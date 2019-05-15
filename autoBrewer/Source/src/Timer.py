from datetime import datetime
import time

def get_time(Duration):
	Current_time = str(datetime.time(datetime.now()))	#gets the current time
	Current_time = Current_time[0:8]	#gets rid of the decimals in the seconds
	Hour = int(Current_time[0:2])	#in case the duration is longer then an hour
	Minutes = int(Current_time[3:5]) + Duration	#calculates the time for end of boil

	while Minutes >= 60:	#loop calculates the correct hours and minutes for the end of boil
		Minutes = Minutes - 60
		Hour+=1
	if Minutes < 10:	#just to make format cleaner
		Minutes = "0"+str(Minutes)
	if Hour > 24:	#ensures time does not go beyond scope
		Hour = Hour - 24
	if Hour < 10:	#just to make format cleaner
		Hour = "0"+str(Hour)
	End_time = str(Hour)+":"+str(Minutes)+Current_time[5:]	#to show user time when boil ends
	print(Current_time)
	print(End_time)
	j = 0	#testing purposes
	while Current_time != End_time:	#loop continues till the boil ends
		Current_time = str(datetime.time(datetime.now())) #gets the current time to eventually end the loop
		Current_time = Current_time[0:8]
		if j == 0:
			print("Running...") #hops dropping program should be running during this time
			j = 1
	print("Success")
	print(Current_time)
###MAIN###
def main():
	Duration = int(input("What is the desired duration in minutes? "))
	get_time(Duration)	#displays time and calculates appropriate time in minutes

if(__name__=='__main__'):
	main()

def my_docstring():
	"""get_time takes user input and formats and calculates the starting and end time of program."""
	pass





