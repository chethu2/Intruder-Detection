import RPi.GPIO as GPIO
import time
import os
import requests
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.IN)

def captureImage():
    os.system('raspistill -o /home/pi/Documents/intruder.jpg')

def ledTrigger():
    print ("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(2)
    print ("LED off")
    GPIO.output(18,GPIO.LOW)

def serverCalls(url,data):
    response = requests.post(url,json=data)
    print (response)

if __name__ == "__main__":
    while True:
        input=GPIO.input(17)
        if input==1:
            print("Intruder Detected")
            captureImage()
            print("capture successful")
            serverCalls("http://localhost:50010/update",{"name":"teamName","url":"http://localhost:8000/intruder.jpg","time":str(datetime.datetime.now())})
            ledTrigger()
        else:
            print("No Intruder")
            time.sleep(1)
