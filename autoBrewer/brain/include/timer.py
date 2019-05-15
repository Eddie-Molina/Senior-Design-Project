#include files
import sys
sys.path.insert(0, '../include')
import threading

import time


#END INCLUDE
class timer:

	#set up variables
	endTime = 0 #holds the timer end variable
	startTime = 0
	on = False #tells us if the timer is running
	deb = 0
	motor = 0
	#set up the timer by passing an end time
	def __init__(self, endingTime, de, mtr):
                """!@brief Creates a new timer object.
        This is what delays the motor until it is time to add the hops
        @param endingTime the number of minutes too have the hops in the boil
        @param de the debugger
        """
                self.endTime = endingTime * 60
                self.deb = de
                self.deb.debugPrint("debug mode in timer")
                self.deb.debugPrint("end time: " + str(self.endTime))
                self.motor = mtr


	def isRunning(self):
                """!@brief checks to see if timer is runnig."""
                return self.on

	def timing(self):
                """!@brief activates the timer
        this is what begins the whole process"""
                self.on = True #we are running now
                startTime = time.time()
                while(1):
                        deltaTime = time.time() - startTime #how much time has ellapsed
                        self.deb.debugPrint("time =" + str(deltaTime))
                        if deltaTime >= self.endTime:
                                self.deb.debugPrint("end", "timer")
                                break
                        time.sleep(0.5)

                self.motor.activate()
                self.on = False #not running
                
                #print("complete")


