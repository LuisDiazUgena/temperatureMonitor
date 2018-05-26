#!/usr/bin/python
import time
import os
import signal
from subprocess import check_output
import re

# Config
minTemp = 65
warning = 0
status = 0
debug = 0
iconState = ""
toggleFile = "/home/pi/temperatureMonitor/Toggle.txt"
PNGVIEWPATH = "/home/pi/temperatureMonitor/Pngview/"
ICONPATH = "/home/pi/temperatureMonitor/icons"
CLIPS = 1
REFRESH_RATE = 2

def changeicon(percent):
    global iconState
    if debug == 1:
        print 'changeicon to ' + percent
    if iconState != percent:
        iconsState = percent
        i = 0
        killid = 0
        os.system(PNGVIEWPATH + "/pngview -b 0 -l 3000" + percent + " -x 10 -y 10 " + ICONPATH +'/'+ percent + ".png &")
        out = check_output("ps aux | grep pngview | awk '{ print $2 }'", shell=True)
        nums = out.split('\n')
        for num in nums:
            i += 1
            if i == 1:
                killid = num
                os.system("sudo kill " + killid)

def endProcess(signalnum=None, handler=None):
    os.system("sudo killall pngview")
    exit(0)

def readTemp():
    out = check_output("/opt/vc/bin/vcgencmd measure_temp", shell=True)
    if debug == 1:
        print "out is "+out
    matchObj = re.match('temp=(\d*.\d*)\'C', out, flags=0)
    if matchObj:
        temp = matchObj.group(1)
        if debug == 1:
            print 'temp is '+temp
        return temp
    else:
        if debug == 1:
            print "unable to find temperature."
        return -1

# Initial Setup

signal.signal(signal.SIGTERM, endProcess)
signal.signal(signal.SIGINT, endProcess)


# Begin Battery Monitoring

os.system(PNGVIEWPATH + "/pngview -b 0 -l 299999 -x 10 -y 10 " + ICONPATH + "/blank.png &")
try:
    with open(toggleFile, 'r') as f:
        output = f.read()
except IOError:
    with open(toggleFile, 'w') as f:
        f.write('1')
    output = '1'
state = int(output)

if state == 1:
    while True:
        try:
            tempF = float(readTemp())
            if tempF > minTemp and tempF != -1:
                if debug == 1:
                    print 'temp after function is' + str(tempF)
                if tempF > 50 and tempF < 55:
                    changeicon("55")
                elif tempF > 55 and tempF < 60:
                    changeicon("60")
                elif tempF > 60 and tempF < 65:
                    changeicon("65")
                elif tempF > 65 and tempF < 70:
                    changeicon("70")
                elif tempF > 70 and tempF < 75:
                    changeicon("75")
                elif tempF > 75 and tempF < 80:
                    changeicon("80")
                elif tempF > 80:
                    changeicon("oh")
                else :
                    changeicon("blank")
            else :
                changeicon("blank")

            # if ret < VOLT0:
            #     if status != 0:
            #         changeicon("0")
            #         if CLIPS == 1:
            #             os.system("/usr/bin/omxplayer --no-osd --layer 999999  " + ICONPATH + "/lowbattshutdown.mp4 --alpha 160;")
            #             os.system("sudo shutdown -h now")
            #     status = 0
            # elif ret < VOLT25:
            #     if status != 25:
            #         changeicon("25")
            #         if warning != 1:
            #             if CLIPS == 1:
            #                 os.system("/usr/bin/omxplayer --no-osd --layer 999999  " + ICONPATH + "/lowbattalert.mp4 --alpha 160")
            #             warning = 1
            #     status = 25
            # elif ret < VOLT50:
            #     if status != 50:
            #         changeicon("50")
            #     status = 50
            # elif ret < VOLT75:
            #     if status != 75:
            #         changeicon("75")
            #     status = 75
            # else:
            #     if status != 100:
            #         changeicon("100")
            #     status = 100

            time.sleep(REFRESH_RATE)
        except IOError:
            print "IOError"
            # print('No i2c Chip Found!')
            # exit(0)

elif state == 0:
    while True:
        try:
            tempF = float(readTemp())
            if tempF > minTemp and tempF != -1:
                if debug == 1:
                    print 'temp after function is' + str(tempF)
                if tempF > 50 and tempF < 55:
                    changeicon("55")
                elif tempF > 55 and tempF < 60:
                    changeicon("60")
                elif tempF > 60 and tempF < 65:
                    changeicon("65")
                elif tempF > 65 and tempF < 70:
                    changeicon("70")
                elif tempF > 70 and tempF < 75:
                    changeicon("75")
                elif tempF > 75 and tempF < 80:
                    changeicon("80")
                elif tempF > 80:
                    changeicon("oh")
                else :
                    changeicon("blank")
            else :
                changeicon("blank")

            time.sleep(REFRESH_RATE)
        except IOError:
            print "IOError"
            # print('No i2c Chip Found!')
            # exit(0)
