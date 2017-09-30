#import packages
from tkinter import *
import time
import numpy as np
import argparse
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera


#initialize values
x1 = 0
x2 = 0
x3 = 0
x4 = 255
x5 = 255
x6 = 255


#define functions
def show_values():
    print(w1.get(), w2.get(), w3.get(), w4.get(), w5.get(), w6.get())


#define sliders
master = Tk()
w1 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w1.set(0)
w1.pack()
w2 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w2.set(0)
w2.pack()
w3 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w3.set(0)
w3.pack()
w4 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w4.set(255)
w4.pack()
w5 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w5.set(255)
w5.pack()
w6 = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w6.set(255)
w6.pack()
Button(master, text='Show', command=show_values).pack()

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    # find the colors within the specified boundaries and apply
    # the mask
    lower = np.array([w1.get(),w2.get(),w3.get()])
    upper = np.array([w4.get(),w5.get(),w6.get()])
    mask = cv2.inRange(image,lower,upper)
    output = cv2.bitwise_and(image,image,mask = mask)

    #update sliders
    master.update_idletasks()
    master.update()
        
 
    # show the frame
    cv2.imshow("Frame", output)
    key = cv2.waitKey(1) & 0xFF
 
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break





