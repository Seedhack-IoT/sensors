#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_PIR=7

GPIO.setup(GPIO_PIR, GPIO.IN)

Current_state = 0
Previous_state = 0

try:
	while GPIO.input(GPIO_PIR)==1:
		Current_state = 0
	print Current_state
	while True:
		Current_state = GPIO.input(GPIO_PIR)
		if Current_state==1 and Previous_state==0:
			print "1"
			Previous_state = 1
		elif Current_state==0 and Previous_state ==1:
			print "0"
			Previous_state = 0

		time.sleep(0.001)

except KeyboardInterrupt:
	print "q"
	GPIO.cleanup()
