import paho.mqtt.client as mqtt
import time
import Adafruit_DHT as adht
import json




# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code {}".format(rc))

client = mqtt.Client()
client.username_pw_set(username = "USERNAME",password = "PASSWORD")
client.on_connect = on_connect
client.connect('IP_ADDRESS', PORT, 60)
client.loop_start()

humidity,temperature = adht.read_retry(adht.DHT22, 4)

if humidity is not None and temperature is not None:
    data = {'temperature': round(temperature, 4),'humidity': int(humidity)}


    client.publish("home/room", json.dumps(data))

    print('Published. Sleeping ...')
else:
    print('Failed to get reading. Skipping ...')
