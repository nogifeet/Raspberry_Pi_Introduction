import RPi.GPIO as gpio
import time
import sys

def init():
     gpio.setmode(gpio.BOARD)
     gpio.setup(7,gpio.OUT)
     gpio.setup(11,gpio.OUT)
     gpio.setup(13,gpio.OUT)
     gpio.setup(15,gpio.OUT)
     
def forward(tf):
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
def reverse(tf):
    init()
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()
    
def turn_left(tf):
    init()
    gpio.output(7,True)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

    
def turn_right(tf):
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
def pivot_left(tf):
    init()
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

    
def pivot_right(tf):
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()
    
input_val = 1

while input_val!=0:
    print("1 - Forward\n 2- Reverse\n 3- Turn Left\n 4-Turn Right\n 5- Pivot Left\n 6-Pivot Right\n")
    inp = int(input("Enter a comand:\n"))
    if inp == 1:
        forward(10)
    elif inp == 2:
        reverse(10)
    elif inp == 3:
        turn_left(3)
    elif inp == 4:
        turn_right(3)
    elif inp == 5:
        pivot_left(3)
    elif inp == 6:
        pivot_right(3)
        
    cnt = input("Do you want to continue?\n Y - Yes and N- No")
    if cnt == 'N':
        input_val = 0
    else:
        pass
    
    
        
    
    
    


    

    