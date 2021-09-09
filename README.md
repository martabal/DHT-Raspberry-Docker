# DHT_Raspberry
Monitor temperature and humidity with your Raspberry, dockers and Grafana

## 1. Connect your DHT with your Raspberry pi with GPIO

Connect gnd, 3.3V and GPIO4

## 2. Edit temperatureloop.sh

Edit temperatureloop.sh with **sudo nano temperatureloop.sh** and change /YOUR/PATH/


## 3. Execute python script on your Raspberry pi

Copy temperature.py and temperatureloops.sh on your raspberry pi and execute temperatureloop.sh on background.
>(Edit DHT11 <em>h,t = adht.read_retry(adht.DHT11, 4)</em> if you use another DHT)


## 4. Create a docker-compose.yml file

Copy docker-compose.yml change paths with yours and start docker-compose with **sudo docker-compose up**

## 5. Configure a data-source in grafana

Click on "Add data source" put your Raspberry pi URL and your Database name (temperature in appadata/Telegraf/telegraf.conf)

## 6. Import my Grafana dashboard

Go on the side menu on Grafana, then Create and click on import. Copy dashboard.json and paste it in the "Import via panel json" section then Load

## 7. Enjoy!



