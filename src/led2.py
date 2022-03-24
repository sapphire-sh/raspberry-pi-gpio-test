import RPi. GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 21

GPIO.setup(LED, GPIO.OUT)

while 1:
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)
