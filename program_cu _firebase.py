import urllib2, urllib, httplib  
import json  
import os   
from functools import partial  
import RPi.GPIO as GPIO
import dht11
import time
  
GPIO.setmode(GPIO.BOARD)  
GPIO.cleanup()  
GPIO.setwarnings(False)  
  
instance = dht11.DHT11(pin=40)   
  
firebase = firebase.FirebaseApplication('https://dht-temperature-6ece4.firebaseio.com/', None)  
  
  
def update_firebase():  
    result = instance.read()
    temperature=result.temperature
    humidity=result.humidity
    if result.is_valid():
        
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
        sleep(5)
    else:  
        print('Failed to get reading. Try again!')    
        sleep(10)  
  
    data = {"temp": temperature, "humidity": humidity}  
    firebase.post('/sensor/dht', data)  
      
  
while True:  
        update_firebase()  
          
        #sleepTime = int(sleepTime)  
        sleep(5)  