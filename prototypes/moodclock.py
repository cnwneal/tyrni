"""
copyright 2011 by Shae Erisson
licensed under the GPLv3
outputs to the mood arduino from page 58 of
http://www.earthshineelectronics.com/files/ASKManualRev5.pdf
"""

import serial
import time

times = [
    ((23,30),'r254 g255 b255'), # sleep
    ((8,0),'g253 r255 b255'), # wakeup
    ((9,0),'b1 r255 g255'), #drive to school
    ]

def setcolor(color):
    print "sending %s to Arduino" % color
    ser = serial.Serial("/dev/ttyUSB0",9600,timeout=1)
    ser.write(color)
    ser.close()

while(1):
    now = time.localtime()
    #(hour,minute) = now.tm_hour,now.tm_min
    nowtuple = now.tm_hour,now.tm_min
    for mood in times:
        if(nowtuple == mood[0]):
            print "matched %s,%s" % mood
            setcolor(mood[1])
    print "sleeping for 30 seconds"
    time.sleep(30)
