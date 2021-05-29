from Event import Event
import apsw
import logging
from collections import deque
from datetime import date, datetime

class Database:
    MAX_CACHE_AGE = 24 * 60 * 60

    # Seconds between updates
    MIN_UPDATE = 1

    def __init__(self, path):
        self.logger = logging.getLogger()

        self._dbPath = path
        connection=apsw.Connection(path)
        self.cursor=connection.cursor()

        # Unknown sensor events, map by the sensor id.
        self.unknownSensorEvents = {}

        # Contains tuples of (min,max) events keyed by event key
        self.minmax = {}

        # Time sensor last seen. Dictionary of sensor id to datetime.
        self.sensorSeen = {}

        self.initCache()
        self.calcCacheMinMax()
 
       
    # Get the location name of a sensor, or Unknown if the sensor is not in the database.
    def getSensorLocationName(self,sensorId):
        result = "Unknown"

        try:
            query = "SELECT location_name FROM sensors JOIN locations using (location_id) WHERE sensor_id=\"{}\"".format(sensorId)
            for (locationName,) in self.cursor.execute(query):
                result = locationName
                self.unknownSensorEvents.pop(sensorId, None)
                self.sensorSeen[sensorId] = datetime.now()
        except Exception as ex:
            self.logger.warning(str(ex))
        
        return result
    
    def getLocationId(self,location):
        result = 0
        try:
            query =  f"SELECT location_id FROM locations WHERE location_name=\"{location}\""
            for (locationId,) in self.cursor.execute(query):
                result = locationId
        
        except Exception as ex:
            self.logger.warning(str(ex))

        return result

    def getSensorLocationId(self,sensorId):
        result = 0
        try:
            query =  f"SELECT location_id FROM sensors WHERE sensor_id=\"{sensorId}\""
            for (locationId,) in self.cursor.execute(query):
                result = locationId
                self.unknownSensorEvents.pop(sensorId, None)
                self.sensorSeen[sensorId] = datetime.now()
         
        except Exception as ex:
            self.logger.warning(str(ex))

        return result

    def createSensor(self,sensorId,location):
        locationId = self.getLocationId(location)
        query=f"INSERT INTO sensors VALUES(\"{sensorId}\",\"{locationId}\");"
        self.logger.info(query)
        try:
            self.cursor.execute(query)
            
            # Remove from unknown events.
            self.unknownSensorEvents.pop(sensorId, None)
        except Exception as ex:
            self.logger.warning(str(ex))

    def deleteSensor(self,sensorId):
        self.logger.info(f"Deleting sensor {sensorId}")
       
        try:
            self.cursor.execute(f"DELETE FROM sensors WHERE sensor_id=\"{sensorId}\"")
            self.sensorSeen.pop(sensorId, None)
            self.unknownSensorEvents.pop(sensorId, None)
        except Exception as ex:
            self.logger.warning(str(ex))

    def deleteClimeMetSensors(self):
        try:
            self.cursor.execute(f"DELETE FROM sensors WHERE length(sensor_id)==3")

        except Exception as ex:
            self.logger.warning(str(ex))

    def deleteUnseenSensors(self):
        try:
            allSensors = [ s for s in self.cursor.execute(f"select sensor_id from sensors") ]
            unseen = set(allSensors) - set(self.sensorSeen.keys())

            for s in unseen:
                self.deleteSensor( s )
        
        except Exception as ex:
            self.logger.warning(str(ex))
     
    def getSensorSeenTime(self,sensorId):
        return self.sensorSeen[sensorId] if sensorId in self.sensorSeen else None

    # return array of (sensor id, location name, last seen)  for all sensors in database and unknowns
    # last seen is datetime, can be Null if not seen.
    def getSensorInfo(self):
        try:
            query = "SELECT sensor_id,location_name FROM sensors JOIN locations using (location_id);"

            result = [ (sensor_id,location_name,self.getSensorSeenTime(sensor_id)) for (sensor_id,location_name) in self.cursor.execute(query) ]
        except Exception as ex:
            self.logger.warning(str(ex))
            result = []

        if len(self.unknownSensorEvents.keys()) != 0:
            unknowns = [ (sensor_id,"Unkown",self.getSensorSeenTime(sensor_id)) for sensor_id in self.unknownSensorEvents.keys()]
            result.extend(unknowns)
        
        return result

    def storeUnknownEvent(self,event):
        self.unknownSensorEvents[event.location()] = event

    def getUnknownEvents(self):
        return self.unknownSensorEvents.values()

    def clearUnknownEvents(self):
        self.unknownSensorEvents.clear()

    def getLocations(self):
        return self.cache.keys()

    def getAllLocations(self):
        result = [ location_name for (location_name,) in self.cursor.execute( 'SELECT location_name FROM locations;' ) ]
        return result

    def handleEvent(self, event):
        if self.cacheEvent(event):
            self.storeEvent(event)

    def getLocationEvents(self,location,meastype):
        if len(meastype) != 0:
            key = (location,meastype)

            if key in self.cache:
                for value in self.cache[ key ]:
                    yield(value)    
        else:
            for key in filter( lambda x : x[0] == location,self.cache.keys()):
                for value in self.cache[ key ]:
                    yield(value)    

    def getLocationClassEvents(self, locationClass):
        #self.logger.info(f"getLocationClassEvents {locationClass}")
        query = f"select location_name from locations JOIN loctype USING (loctype_id) WHERE loctype_name=\"{locationClass}\";"
        #self.logger.info(f"query={query}")

        locations = [ location_name for (location_name,) in self.cursor.execute( query ) ]

        #self.logger.info(f"locations={locations}")

        keys =  filter( lambda x : x[0] in locations, self.cache.keys())
        for key in keys:
            for value in self.cache[ key ]:
                yield(value)    

    def getAllEvents(self):        
        for x in self.cache.values():
            yield(x)

    # Get min, max, latest for each location
    def getSummaryEvents(self):
        events = []
        for k in self.cache.keys():
            events.append(self.minmax[k][0])
            events.append(self.minmax[k][1])
            events.append(self.cache[k][-1])
        return events

    def storeEvent(self,event):
        locationId = self.getLocationId(event.location())
        
        self.logger.warning(f"Failed to map location {event.location()}") if locationId == 0 else None

        try:
            self.logger.info("Write event to database.")
            command = f"INSERT INTO readings( timestamp,location_id,desc,value) VALUES('{event.timestamp()}',{locationId},'{event.desc()}',{event.value()});"
            self.logger.info(command)
            self.cursor.execute(command)
        
        except Exception as ex:
            self.logger.warning(str(ex))
    
    # Return True if the event was cached and is a candidate to store in DB.
    def cacheEvent(self,event):

        # Default store to cache unless filtered for too high frequency.
        storeToCache = True
        storeToDB = True

        key = event.getKey()

        self.logger.debug(f"cacheEvent for {event}.")

        #
        if not key in self.cache:
            self.logger.debug(f"No entries for {key}. Create deque.")
            self.cache[ key] = deque()

        # Filter high frequency events.
        if storeToDB and len(self.cache[ key ]) > 0:
            timeDelta = (event.time() - self.cache[ key ][-1].time()).total_seconds()
            storeToDB = timeDelta >= Database.MIN_UPDATE
            self.logger.debug(f"storeToDB {storeToDB} for age delta {timeDelta}")

            # Don't store duplicates
            if self.cache[ key ][-1].value() == event.value():
                # Special case Pressure, changes so little, logged every 15 mins.
                if key[1] != "Pressure":
                    self.logger.debug(f"Duplicate; suppress store to DB")
                    storeToDB = False
 
        if storeToCache:
            self.logger.debug(f"Write to cache.")

            self.cache[ key ].append(event)
            self.updateMinMax(event)

            if self.flushCache():
                self.calcCacheMinMax(key)

        return storeToDB

    # Return True if min/max change.
    def updateMinMax( self,event ):
        key = event.getKey()
        chg = False

        if key in self.minmax:
            (minEvt,maxEvt) = self.minmax[key]
            #self.logger.debug(f"updateMinMax...old values for {key} min={minEvt.value()} max={maxEvt.value()}")
            (maxEvt,chg) = (event,True or chg) if event.value() > maxEvt.value() else (maxEvt,False and chg)
            (minEvt,chg) = (event,True or chg) if event.value() < minEvt.value() else (minEvt,False and chg)

            #self.logger.debug(f"updateMinMax...change {chg} for {key} min={minEvt.value()} max={maxEvt.value()}")
        else:
            (minEvt,maxEvt,chg) = (event,event,True)
            #self.logger.debug(f"updateMinMax...new entry for {key} min={minEvt.value()} max={maxEvt.value()}")

        self.minmax[key] = (minEvt, maxEvt)

        if chg:
            self.logger.debug(f"updateMinMax...for {key} min={minEvt.value()} max={maxEvt.value()}")
        
        return chg

    def getMinimumEvents(self,key=None):
        if key is None:
            return [ x[0] for x in self.minmax.values()]
        else:
            return self.minmax[key][0] if key in self.minmax else None

    def getMaximumEvents(self,key=None):
        if key is None:
            return [ x[1] for x in self.minmax.values()]
        else:
            return self.minmax[key][1] if key in self.minmax else None

    def calcCacheMinMax(self, key = None):
        self.logger.debug("calcCacheMinMax")

        keys = self.cache.keys() if key == None else [ key ]

        for k in keys:
            minValue = min( self.cache[k],key=lambda x : x.value() )
            maxValue = max( self.cache[k],key=lambda x : x.value() )
            self.minmax[k]=( minValue, maxValue )

            self.logger.info(f"For {k} min={self.minmax[k][0].value()} max={self.minmax[k][1].value()}")

    def flushCache(self):
        changed = False

        now = datetime.now()

        # For each event queue, throw away anything older than the max time we keep for.
        for eventQueue in self.cache.values():
            while len(eventQueue) > 0 and (now - eventQueue[ 0 ].time()).total_seconds() > Database.MAX_CACHE_AGE:
                eventQueue.popleft()
                changed = True

        return changed

    def initCache(self):
       # Cache recent Events by key (Location,Description) tuple indexing deques of events.
        self.cache = {} 

        self.logger.debug(f"initCache")
        try:
            query =  "SELECT timestamp,location_name,desc,value from readings JOIN locations using (location_id) " \
                     "where  timestamp>date('now','-1 day') ORDER BY timestamp ASC;"
            for (timestamp,location,desc,value) in self.cursor.execute(query):
                #self.logger.debug(f"Build event from {timestamp},{location},{desc},{value}")
                event = Event(location,desc,value,timestamp )
                if not event.getKey() in self.cache:
                    self.cache[event.getKey()] = deque()
                self.cache[event.getKey()].append(event)

        except Exception as ex:
            self.logger.error(str(ex))

        self.logger.debug(f"initCache complete")

    def getLatestEvents(self):
        return [ x[-1] for x in self.cache.values() ]

    def getLocations(self):
        return self.cache.keys()
