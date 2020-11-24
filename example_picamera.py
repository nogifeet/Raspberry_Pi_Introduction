import picamera
import time

def capture_single(flip=0):
    #capture a single image using PiCamera
    camera = picamera.PiCamera()
    if flip==1:
        #cause the camera to vertically flip
        camera.vflip = True
        camera.capture('example1_flip_1.jpg')
    else:
        camera.capture('example1_1.jpg')
    
#capture_single(flip=1)
        
def capture_multiple():
    #capture multiple images using picamera
    camera = picamera.PiCamera()
    camera.vflip = True
    for i in range(5):
        camera.capture(f'example_{i}.jpg')

#capture_multiple()
        
def capture_video():
    #record video using PiCamera
    camera = picamera.PiCamera()
    camera.vflip = True
    camera.start_recording('example_vid.h264')
    time.sleep(10)
    camera.stop_recording()
    
#capture_video()
    
def capture_preview():
    camera = picamera.PiCamera()
    camera.vflip = True
    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    
#capture_preview()
    

    
