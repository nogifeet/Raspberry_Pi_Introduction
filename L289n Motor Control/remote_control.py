import RPi.GPIO as gpio
import picamera
import time
import io
import socket
import struct
import sys
import tkinter as tk
         
def init():
     gpio.setmode(gpio.BOARD)
     gpio.setup(7,gpio.OUT)
     gpio.setup(11,gpio.OUT)
     gpio.setup(13,gpio.OUT)
     gpio.setup(15,gpio.OUT)
     
def forward(tf):
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
def reverse(tf):
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()
    
    
def turn_left(tf):
    gpio.output(7,True)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

    
def turn_right(tf):
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
def pivot_left(tf):
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

    
def pivot_right(tf):
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()
    
def distance():
    trig = 35
    echo=37
    gpio.setmode(gpio.BOARD)
    gpio.setup(trig,gpio.OUT)
    gpio.setup(echo,gpio.IN)
    
    while True:
    
        gpio.output(trig, True)
        time.sleep(0.00001)
        gpio.output(trig, False)
        
        while gpio.input(echo)==0:
            
            pulse_start = time.time()
            
        while gpio.input(echo) ==1:
            
            pulse_end = time.time()
            
        pulse_dur = pulse_end-pulse_start
        distance = (pulse_dur *34000)/2
        return round(distance,2)        
    
def key_input(event):
    #allowed_keys = ['w','a','s','d','e','q']
    init()
    print("Key: {}".format(event.char))
    key_press = event.char
    sleep_time = 0.030
    
    if key_press.lower() == 'w':
        forward(sleep_time)
        
    elif key_press.lower() == 's':
        reverse(sleep_time)
    
    elif key_press.lower() == 'a':
        turn_left(sleep_time)
    
    elif key_press.lower() == 'd':
        turn_right(sleep_time)
        
    elif key_press.lower() == 'q':
        pivot_left(sleep_time)
        
    elif key_press.lower() == 'e':
        pivot_right(sleep_time)
        
    else:
        gpio.cleanup()
        
    obs_dist = distance()
    #print("Distance is {}".format(obs_dist))
    
    if obs_dist<10:
        init()
        forward(3)

    

command = tk.Tk()
command.bind('<KeyPress>' , key_input)
command.mainloop()


    
    
    
    
    
        


    

    