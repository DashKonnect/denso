import serial
from time import sleep
import sys
import numpy as np
import os

COM = '/dev/ttyACM0'# /dev/ttyACM0 (Linux)
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout = .1)

X = []
Y = []
print('Waiting for device');
print(ser.name)

#check args
if("-m" in sys.argv or "--monitor" in sys.argv):
	monitor = True
else:
	monitor= False


file_name = 'training_data.npy'
if os.path.isfile(file_name):
	print('File exists, loading previous data!')
	training_data = list(np.load(file_name))
else:
	print('File does not exist, starting fresh!')
	training_data = []

print("enter class number [1:wood,2:laptop,3:book] to start storing reading")
v = input()
output = int(v)
count = 0
count_turns = 0
data = list()
while count_turns < 100:
	val = str(ser.readline().decode().strip('\r\n'))#Capture serial output as a decoded string
	valA = val.split("/")
	if(monitor == True):
		if val != '':
			print (count,float(val))
			data.append(float(val))
			count +=1

	if count == 10:
		count_turns += 1
		print(data)
		training_data.append([data,v])
		count = 0
		data = []
		np.save(file_name,training_data)
		print("Next Reading....")
		sleep(2)

