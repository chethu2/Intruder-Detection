import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

def ledTrigger():
    print ("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print ("LED off")
    GPIO.output(18,GPIO.LOW)
    time.sleep(1)

if __name__ == "__main__":
    while True:
        ledTrigger()

