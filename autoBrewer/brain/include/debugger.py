

import threading
import sys
from termcolor import colored

'''
The debugger class is made to make the work flow simpler.
allows easy colored outputs while printing.


'''
class debugger:
	on = False
	
	def __init__(self):
                """!@brief Creates a debugger object.
        allows us to more easily run debug prints"""
                self.on = False

	def activate(self):
                self.on = True

	def debugPrint(self, msg, header = ""):
                print_lock = threading.Lock()
		#print(str(self.on))
                listMsg = ""
                with print_lock:
                        if(self.on):
                                if(type(msg) is list):
                                        for item in msg:
                                                print(item)
                                #listMsg = listMsg + "\n\t" + str(item)
                        
               
                                else:
                                        print(colored('DEBUGGER:', 'red'))
                                        print(colored(header, 'yellow'))
                                        print(colored('\t' + msg,'green'))
		
