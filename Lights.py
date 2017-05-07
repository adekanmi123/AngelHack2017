#!/usr/bin/python

import thread
import time
import serial
import json
import urllib2

eflag='1'
dflag='1'

ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
ser.write("grrr")
ser.write("grrr")
ser.write("grrr")
ser.write("grrr")


# Define a function for the thread
def light_display( threadName):
	
	time.sleep(3)
	ser.write("grrr")
	time.sleep(10)
	ser.write("yrrr")
	time.sleep(3)
	ser.write("ryrr")
	time.sleep(3)
	ser.write("rgrr")
	time.sleep(10)
	ser.write("ryrr")
	time.sleep(3)
	ser.write("rryr")
	time.sleep(3)
	ser.write("rrgr")
	time.sleep(10)
	ser.write("rryr")
	time.sleep(3)
	ser.write("rrry")
	time.sleep(3)
	ser.write("rrrg")
	time.sleep(10)
	ser.write("rrry")
	time.sleep(3)
	ser.write("yrrr")

	
      
def light_control( threadName):
	
	response = urllib2.urlopen('http://gsarora.in/ah10/index.php?request=get&light')
	html=response.read()
	html = json.loads(html)
	signal=html['result']['light']
	eflag=html['result']['eflag']
	dflag=html['result']['dflag']
	print signal
	print eflag
	print dflag
	time.sleep(3)
   	
# Create two threads as follows
try:
   thread.start_new_thread( light_display, ("thread_1", ) )
   thread.start_new_thread( light_control, ("thread_2", ) )
except:
   print "Error: unable to start thread"

i=0;
while 1:
   pass
   if eflag==1 and dflag==1:
   		ser.write("rrrr")
   		time.sleep(2);
   		ser.write("gggg")
		thread_1.exit()
   			
   