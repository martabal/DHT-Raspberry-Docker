#!/bin/bash

while [ : ]
do
    clear
    cd /YOUR/PATH/script/temp && sudo python3 temperature.py
    sleep 2
    echo "Sleeping..."
    sleep 60
done
