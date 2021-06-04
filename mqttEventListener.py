import paho.mqtt.client as mqtt
import argparse
import logging
import json

import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

import dsws_pb2
import dsws_pb2_grpc

LogLevels = { "CRITICAL" : 50, "ERROR" : 40, "WARNING" : 30, "INFO" : 20, "DEBUG" : 10 }

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, stub, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Temperature")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, stub, msg):
    logging.info(msg.topic+" "+str(msg.payload))

    payload = json.loads(msg.payload)

    if "type" in payload.keys() and "sensor" in payload.keys() and "val" in payload.keys():
        stub.NotifySensorEvent(
                        dsws_pb2.SensorEvent(
                            Sensor=payload["sensor"],
                            MeasType=payload["type"],
                            MeasValue=payload["val"]),
                        timeout=10)
    else:
        logging.warn("Unable to process " + str(msg.payload))

    # If RSSI piggybacked on the measurement, add that too.
    if "type" in payload.keys() and "sensor" in payload.keys() and "rssi" in payload.keys():
        stub.NotifySensorEvent(
                        dsws_pb2.SensorEvent(
                            Sensor=payload["sensor"],
                            MeasType="RSSI",
                            MeasValue=payload["rssi"]),
                        timeout=10)
    
    # If Battery (voltage) piggybacked on the measurement, add that too.
    if "type" in payload.keys() and "sensor" in payload.keys() and "battery" in payload.keys():
        stub.NotifySensorEvent(
                        dsws_pb2.SensorEvent(
                            Sensor=payload["sensor"],
                            MeasType="Voltage",
                            MeasValue=payload["battery"]),
                        timeout=10)

def mqttListener(server,port):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("webpi2", 1883, 60)

    with grpc.insecure_channel(target="{}:{}".format(server, port),
                        options=[('grpc.lb_policy_name', 'pick_first'),
                                ('grpc.enable_retries', 0),
                                ('grpc.keepalive_timeout_ms', 10000)
                                ]) as channel:
        
        stub = dsws_pb2_grpc.EventServerStub(channel)

        client.user_data_set( stub )

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-S", "--server", help="Server Name", default="webpi2")
    parser.add_argument("-P", "--port", type=int, help="Server Port", default=50051)

    parser.add_argument("-l", "--log-level", dest="log_level", default="WARNING",choices=LogLevels.keys(),help="Set Python logging level")

    args = parser.parse_args()

    logging.basicConfig(level=LogLevels[args.log_level])

    mqttListener( args.server, args.port )

if __name__ == "__main__":
    # execute only if run as a script
    main()
