import RPi.GPIO as gpio
import time
 
gpio.setmode(gpio.BCM)
gpio.setup(24,gpio.OUT)
pwm = gpio.PWM(24,50) #servos like 50hz frequency
pwm.start(5)

def run_servo(angle):

    duty = 1./20.*(angle)+2
    print("Turning motor at angle {}".format(angle))
    pwm.ChangeDutyCycle(duty)

angle=[0,45,90,135,180,0]
for i in angle:
    run_servo(i)
    time.sleep(2)
    
pwm.stop()
gpio.cleanup()
    

    


