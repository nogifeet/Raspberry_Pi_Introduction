#led example for traffic Signal
#each signal will be lit for 10 seconds then turn off(except Yellow)
#the signal will run for 5 interations
#order Red-10 seconds, Yellow - 5 Seconds, Green - 10 Seconds similar to Real Life Traffic Signal

#Pin Structure
#GPIO-18 for Green
#GPIO-17 for Yellow
#GPIO-23 for Red

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#set output pins
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

for i in range(3):
    #turn on the red signal for 10 sec
    GPIO.output(23, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(23, GPIO.LOW)
    
    #turn on the yellow signal for 5 sec
    GPIO.output(17, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(17, GPIO.LOW)
    
    #turn on the green signal for 10 sec
    GPIO.output(18, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(18, GPIO.LOW)
    
GPIO.cleanup()

