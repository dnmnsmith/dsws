from concurrent import futures
import logging
import argparse

import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

import dsws_pb2
import dsws_pb2_grpc
from pathlib import Path

from Database import Database
from Event import Event

SERVER_ID = 1
LogLevels = { "CRITICAL" : 50, "ERROR" : 40, "WARNING" : 30, "INFO" : 20, "DEBUG" : 10 }


empty = google_dot_protobuf_dot_empty__pb2.Empty()

class EventHandler(dsws_pb2_grpc.EventServer):
    def __init__(self,database):
        self.database = database

    def makeGrpcEvent(e):
        return dsws_pb2.Event(
                    DateTime = e.time().isoformat(),
                    Location = e.location(),
                    MeasType = e.desc(),
                    MeasValue = str(e.value()))

    def NotifyLocationEvent(self,request,context):
        event = Event( location = request.Location, desc=request.MeasType, value=request.MeasValue)
        logging.debug("Location Event Received " + str(event))
        self.database.handleEvent(event)
        return empty

    def NotifySensorEvent(self,request,context):
        locationName = self.database.getSensorLocationName(request.Sensor)
        if locationName == 'Unknown':
            logging.warning(f"Unknown sensor id {request.Sensor}")
            event = Event( location = request.Sensor, desc=request.MeasType, value=request.MeasValue)
            logging.info("Sensor Event Received " + str(event))
            self.database.storeUnknownEvent(event)
        else:
            event = Event( location = locationName, desc=request.MeasType, value=request.MeasValue)
            logging.info("Sensor Event Received " + str(event))
            self.database.handleEvent(event)

        return empty

    def GetLatestEvents(self,request,context):
        def response_messages():
            for e in self.database.getLatestEvents():
                yield EventHandler.makeGrpcEvent( e )
        return response_messages()

    def GetMinimumEvents(self,request,context):
        def response_messages():
            for e in self.database.getMinimumEvents():
                yield EventHandler.makeGrpcEvent( e )
        return response_messages()

    def GetMaximumEvents(self,request,context):
        def response_messages():
            for e in self.database.getMaximumEvents():
                yield EventHandler.makeGrpcEvent( e )
        return response_messages()

    def GetUnknownEvents(self,request,context):
        def response_messages():
            for e in self.database.getUnknownEvents():
                yield EventHandler.makeGrpcEvent( e )
        return response_messages()

    def ClearUnknownEvents(self,request,context):
        self.database.clearUnknownEvents()
        return empty

    def GetAllLocations(self,response,context):
        def response_messages():
            for location in self.database.getAllLocations():
                yield dsws_pb2.LocationName(Location = location)
        return response_messages()

    def GetLocations(self,response,context):
        def response_messages():
            for location in self.database.getLocations():
                yield dsws_pb2.Location(
                    Location = location[0],
                    MeasType = location[1])

        return response_messages()

    def GetLocationEvents(self,request,context):
        def response_messages():
            for e in self.database.getLocationEvents(request.Location, request.MeasType):
                yield EventHandler.makeGrpcEvent( e )
        return response_messages()

    def GetLocationClassEvents(self,request,context):
        def response_messages():
            for e in self.database.getLocationClassEvents( request.LocationClass ):
                yield EventHandler.makeGrpcEvent( e )
        return response_messages()

    # Get min,max,latest events for each location
    def GetSummaryEvents(self,request,context):
        def response_messages():
            for e in self.database.getSummaryEvents():
                yield EventHandler.makeGrpcEvent( e )
        return response_messages()

    def GetAllEvents(self,request,context):
        def response_messages():
            for e in self.database.getAllEvents():
                yield EventHandler.makeGrpcEvent( e )
        return response_messages()

    def ConfigSensor( self,request,context):
        self.database.createSensor(request.SensorId,request.Location)
        return empty

    def DeleteSensor( self,request,context):
        self.database.deleteSensor( request.SensorId )
        return empty

    def DeleteClimeMet(self,request,context):
        self.database.deleteClimeMetSensors( )
        return empty

    def DeleteUnseenSensors(self,request,context):
        self.database.deleteUnseenSensors( )
        return empty

    def GetSensorInfo(self,request,context):
        logging.info("GetSensorInfo")
        def response_messages():
            for (sensorId,location,time) in self.database.getSensorInfo():
                timeString = time.isoformat() if not time is None else ""
                yield dsws_pb2.SensorInfo( 
                    SensorId=sensorId,
                    Location=location,
                    LastSeen=timeString )
        return response_messages()     

def serve(port,database):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dsws_pb2_grpc.add_EventServerServicer_to_server(EventHandler(database), server)
    server.add_insecure_port('[::]:{}'.format(port))
    print("Starting server on port {}".format(port))
    server.start()
    server.wait_for_termination()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--database", help="Database Path",default="/var/local/events.db")
    parser.add_argument("-p", "--port", type=int, help="Server Port", default=50051)
    parser.add_argument("-l", "--log-level", dest="log_level", default="WARNING",choices=LogLevels.keys(),help="Set Python logging level")
    args = parser.parse_args()

    logging.basicConfig(level=LogLevels[args.log_level])

    database = Database( args.database )

    serve(args.port,database)

if __name__ == '__main__':
    main()

