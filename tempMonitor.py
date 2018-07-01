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
PNGVIEWPATH = "/home/pi/temperatureMonitor/Pngview"
ICONPATH = "/home/pi/temperatureMonitor/icons"
CLIPS = 1
REFRESH_RATE = 3

def changeicon(percent):
    global iconState
    if debug == 1:
        print 'changeicon to ' + percent
    if iconState != percent:
        iconsState = percent
        i = 0
        killid = 0
        os.system(PNGVIEWPATH + "/pngview -b 0 -l 3000" + percent + " -x 0 -y 10 " + ICONPATH +'/'+ percent + ".png &")
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

os.system(PNGVIEWPATH + "/pngview -b 0 -l 299999 -x 0 -y 10 " + ICONPATH + "/blank.png &")
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
                if tempF > 50 and tempF < 51.5:
                    changeicon("50")
                elif tempF > 51 and tempF < 52.5:
                    changeicon("51")
                elif tempF > 52 and tempF < 53.5:
                    changeicon("52")
                elif tempF > 53 and tempF < 54.5:
                    changeicon("53")
                elif tempF > 54 and tempF < 55.5:
                    changeicon("54")
                elif tempF > 55 and tempF < 56.5:
                    changeicon("55")
                elif tempF > 56 and tempF < 57.5:
                    changeicon("56")
                elif tempF > 57 and tempF < 58.5:
                    changeicon("57")
                elif tempF > 58 and tempF < 59.5:
                    changeicon("58")
                elif tempF > 59 and tempF < 60.5:
                    changeicon("59")
                elif tempF > 60 and tempF < 61.5:
                    changeicon("60")
                elif tempF > 61 and tempF < 62.5:
                    changeicon("61")
                elif tempF > 62 and tempF < 63.5:
                    changeicon("62")
                elif tempF > 63 and tempF < 64.5:
                    changeicon("63")
                elif tempF > 64 and tempF < 65.5:
                    changeicon("64")
                elif tempF > 65 and tempF < 66.5:
                    changeicon("65")
                elif tempF > 66 and tempF < 67.5:
                    changeicon("66")
                elif tempF > 67 and tempF < 68.5:
                    changeicon("67")
                elif tempF > 68 and tempF < 69.5:
                    changeicon("68")
                elif tempF > 69 and tempF < 70.5:
                    changeicon("69")
                elif tempF > 70 and tempF < 71.5:
                    changeicon("70")
                elif tempF > 71 and tempF < 72.5:
                    changeicon("71")
                elif tempF > 72 and tempF < 73.5:
                    changeicon("72")
                elif tempF > 73 and tempF < 74.5:
                    changeicon("73")
                elif tempF > 74 and tempF < 75.5:
                    changeicon("73")
                elif tempF > 75 and tempF < 76.5:
                    changeicon("75")
                elif tempF > 76 and tempF < 77.5:
                    changeicon("76")
                elif tempF > 77 and tempF < 78.5:
                    changeicon("77")
                elif tempF > 78 and tempF < 79.5:
                    changeicon("78")
                elif tempF > 79 and tempF < 80.5:
                    changeicon("79")
                elif tempF > 80 and tempF < 81.5:
                    changeicon("79")
                elif tempF > 81 and tempF < 82.5:
                    changeicon("79")
                elif tempF > 82 and tempF < 83.5:
                    changeicon("79")
                elif tempF > 83 and tempF < 84.5:
                    changeicon("79")
                elif tempF > 84 and tempF < 85.5:
                    changeicon("79")
                elif tempF > 85:
                    changeicon("80")
                else :
                    changeicon("blank")
            else :
                changeicon("blank")
            time.sleep(REFRESH_RATE)
        except IOError:
            print "IOError"
elif state == 0:
    while True:
        try:
            tempF = float(readTemp())
            temp = string(int(float(readTemp)))
            if temp > minTemp and tempF != -1 and tempF > 50 and tempF<100:
                changeicon(temp)
            else :
                changeicon("blank")

            time.sleep(REFRESH_RATE)
        except IOError:
            print "IOError"
