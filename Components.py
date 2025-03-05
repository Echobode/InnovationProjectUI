import RPi.GPIO as GPIO 
import threading
import time
import asyncio

class Components:
	def __init__(self):
		GPIO.setmode( GPIO.BCM )
		GPIO.setwarnings( False )
		self.solenoidGPIO = 26
		GPIO.setup( self.solenoidGPIO, GPIO.OUT )
		
	def clean_all(self): 
		GPIO.cleanup()
	
	def activate_solenoid(self):
		GPIO.output( self.solenoidGPIO, GPIO.HIGH )


	
	def deactivate_solenoid(self):
		GPIO.output( self.solenoidGPIO, GPIO.LOW )		
		
	def activate_solenoid_async(self):
		self.activate_solenoid()
		time.sleep(1.5)
		self.deactivate_solenoid()

		
