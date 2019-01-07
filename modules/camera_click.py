import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

if __name__ == '__main__':
    time.sleep(1)
    print("triggering camera action")
    os.system('raspistill -o /home/pi/Desktop/new.jpg')
