#!/bin/bash

cd ~
sudo apt-get update
sudo apt-get install libpng12-dev -y
sudo apt-get install python-gpiozero -y
sudo apt-get install python-pkg-resources python3-pkg-resources -y
sudo apt-get install build-essential python-dev python-smbus python-pip -y
cd ~
sudo chmod 755 /home/pi/temperatureMonitor/Pngview/pngview
sudo sed -i '/\"exit 0\"/!s/exit 0/\(sudo python \/home\/pi\/temperatureMonitor\/tempMonitor.py) \&\nexit 0/g' /etc/rc.local
