#!/usr/bin/env python

global DEBUG #debug flag
#include files
import sys
sys.path.insert(0, '/home/pi/Documents/autoBrewer/brain/include/')
#sys.path.insert(0, '/home/pi/Documents/sdProject/autoBrewer/brain/include')
from timer import *
from debugger import *
import RPi.GPIO
from motor import *
import os
import glob
import time


#END INCLUDE
#define pin numbers for the motors
MOTOR1 = 8
MOTOR2 = 10
MOTOR3 = 12
MOTOR4 = 16
MOTOR5 = 18
MOTOR6 = 22

#temperature sensor stuff

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        
        return temp_c 
    

#end temp sensor stuff

GPIO.setmode(GPIO.BOARD)  # set board mode to Broadcom

motorPins = [MOTOR1,MOTOR2,MOTOR3,MOTOR4,MOTOR5, MOTOR6]
motors = []

myDe = debugger()
print_lock = threading.Lock()
timers = []
times = []
temp = 0
def main():
    arguments = sys.argv #pull in arguments
    counter = 0
    numExpected = False
    tempExpected = False

        
    for item in arguments:
            if (numExpected):
                data = item.split('/')
                times.append(float(data[1]))
                myDe.debugPrint(times)
                mtrNum = int(data[0])
                motors.append(motor(motorPins[mtrNum-1], myDe, mtrNum))
                print(times)
                print(mtrNum)
                numExpected = False
            if (tempExpected):
                data = item.split('/')
                temperatureHold = float(data[1])
                times.append(0)
                myDe.debugPrint(times)
                mtrNum = int(data[0])
                motors.append(motor(motorPins[mtrNum-1], myDe, mtrNum, True, temperatureHold))
                print(times)
                print(mtrNum)
                tempExpected = False

                
        #print(item)  
            if(item == "-D" or item == "-d"):
                myDe.activate()
                myDe.debugPrint(item, "input " + str(counter))
                counter = counter + 1
            if(item.startswith("-t")):
                myDe.debugPrint("found timer input in minutes")
                numExpected = True
            if(item.startswith("-a")):
                myDe.debugPrint("temp Input")
                tempExpected = True
    count = 0
    for tm in times:
            if(tm == 0):
                count += 1
                continue
            newTimer = timer(tm, myDe, motors[count])
            timers.append(newTimer)
            count += 1
    #myDe.debugPrint("Debugger Activated")
    for i in range(0, len(timers)):
            t = threading.Thread(target = beginTimer, args=(i,))
            t.daemon = True
            t.start()
    activeTimers = True
    time.sleep(3)
    while(activeTimers):
            activeTimers = False
            message = "Current Temp = " + str(read_temp())
            myDe.debugPrint(message)
            for tmr in timers:
                print(tmr.isRunning())
                if (tmr.isRunning()):
                    activeTimers = True
            time.sleep(1)
    afterBrewHopping = True

    while(afterBrewHopping):
            afterBrewHopping = False
            for mtr in motors:
                message = "Current Temp = " + str(read_temp())
                myDe.debugPrint(message)
                if(mtr.testTemp() != False):
                    tempToFind = mtr.testTemp()
                    curTemp = read_temp()
                    if(tempToFind >= curTemp):
                        message = "curtemp: " + str(read_temp()) + " <g activate temp: " + str(mtr.testTemp())
                        myDe.debugPrint(message)
                        mtr.activate()
                        mtr.deactivate()
                    else:
                        afterBrewHopping = True
                        message = "curtemp: " + str(read_temp()) + " > activate temp: " + str(mtr.testTemp())
                        myDe.debugPrint(message)
                    time.sleep(1)

def beginTimer(index):
    myDe.debugPrint("testing")
    timers[index].timing()







#print("test failed")

if __name__ == '__main__':
    DEBUG = False
    main()
