import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 21
ECHO = 20
distance_count=0

while distance_count<=10:

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    #calculate how much time it took for the signal to travel
    #from the TRIGGER and received by the ECHO

    while GPIO.input(ECHO) == False:
        start = time.time()
        
    while GPIO.input(ECHO) == True:
        end = time.time()
        
    sig_time = end-start

    #cm distance calculation
    distance = sig_time/0.000058

    #for inches use: 0.000148
    print('Distance: {} cm'.format(distance))
    distance_count+=1
    time.sleep(2)
    
    #calculate distance using another login
    #pulse_dur = end-start
    #distance = (pulse_dur *34000)/2
    #print("Distnace is {}".format(round(distance,2)))
    #time.sleep(1)
    


GPIO.cleanup()
