import Adafruit_DHT as adht
import time
from datetime import datetime
from influxdb import InfluxDBClient

json_payload = []
current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

h,t = adht.read_retry(adht.DHT22, 4)


data = {
  "measurement": "room_temperature_humidity",
  "tags": {
    "location": "YOUR ROOM",
},
  "time": current_time,
  "fields": {
    "temperature":round(float(t),2),
    "humidity":round(float(h),2),
  }
}
json_payload.append(data)
client = InfluxDBClient(HOST_IP, HOST_PORT, 'INFLUXDB_USERNAME', 'INFLUXDB_PASSWORD', 'DATABASE_NAME')
client.write_points(json_payload)
print(data)
