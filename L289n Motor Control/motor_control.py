import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def init():
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)

def forward():
    init()
    GPIO.output(22,False)
    GPIO.output(27,True)
    GPIO.output(17,True)
    GPIO.output(4,False)
    time.sleep(5)
    
def backward():
    init()
    GPIO.output(22,True)
    GPIO.output(27,False)
    GPIO.output(17,False)
    GPIO.output(4,True)
    time.sleep(5)
    
def right():
    init()
    GPIO.output(22,False)
    GPIO.output(27,False)
    GPIO.output(17,True)
    GPIO.output(4,True)
    time.sleep(5)
    
def left():
    init()
    GPIO.output(22,True)
    GPIO.output(27,True)
    GPIO.output(17,False)
    GPIO.output(4,False)
    time.sleep(5)
    
left()
right()
forward()
backward()

GPIO.cleanup()

