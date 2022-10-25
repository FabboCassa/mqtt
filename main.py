#mqtt_sub
import json
import time
from collections import namedtuple

from paho.mqtt import client as mqtt_client

def customJsonDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())

def on_message(client, userdata, message):
    print("received message =",str(message.payload.decode("utf-8")))
    response = json.loads(message.payload, object_hook=customJsonDecoder)
    print(f"Name: {response.name}\nAddress: {response.address}")


Connected = False
broker = 'test.mosquitto.org'
port=1883
topic = "milan"
client =mqtt_client.Client()

client.on_message= on_message
client.connect(broker, port)
client.loop_start()  # start the loop

client.subscribe("milan")


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
