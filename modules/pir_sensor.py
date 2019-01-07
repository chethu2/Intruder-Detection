import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

def startSensing():
    print("No intruder")

if __name__ == '__main__':
    while True:
        input = GPIO.input(18)
        if input==1:
            print("intruder detected")
            time.sleep(1)
        else:
            print("no intruder")
            time.sleep(1)
