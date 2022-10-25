from paho.mqtt import client as mqtt_client
import json

client = mqtt_client.Client()


class azienda:
    def __init__(self, name, address, boss, workers, women):
        self.name = name
        self.address = address
        self.boss = boss
        self.workers = workers
        self.women = women


# with open('C:\\Users\\fitstic\\Desktop\\dummy_JSON.json') as dummy_json:
AZ1 = azienda("PyTech", "Direzionale 70", "Alessandro Grandi", 10, True)
my_json_obj = json.dumps(AZ1, default=lambda o: o.__dict__,
                         indent=4)
client.connect('test.mosquitto.org', 1883, 60)
client.publish("milan", my_json_obj)
client.disconnect()
