#The objective is to use distance sensor to calculate distance
#Use Led lights to indicate distance as output
# Distance > 50 use Green Light
# 10 <= Distance <= 50 Yellow Light
# Distance < 10 Red Light

#Pin Structure
#GPIO-18 for Green
#GPIO-17 for Yellow
#GPIO-23 for Red
#Sensor TRIGGER - 21
#Sensor ECHO - 20

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 21
ECHO = 20
GREEN = 18
YELLOW = 17
RED = 23
count=0

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)


#function to calculate distance in cm
def calculate_distance(end,start):
    sig_time = end-start

    #cm distance calculation
    distance = sig_time/0.000058
    
    return round(distance,2)

while count<5:
    
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == False:
        start = time.time()
        
    while GPIO.input(ECHO) == True:
        end = time.time()
        
    d = calculate_distance(end,start)
    
    if d < 10:
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(RED, GPIO.LOW)
    
    elif d<=50:
        GPIO.output(YELLOW, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(YELLOW, GPIO.LOW)
    
    elif d>50:
        GPIO.output(GREEN, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(GREEN, GPIO.LOW)
        
    count+=1
    
GPIO.cleanup()
        
    
    
    
    
    
    
    