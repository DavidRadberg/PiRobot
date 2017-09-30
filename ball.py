# import the necessary packages
import numpy as np
import argparse
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)

#define boundaries
bound = [
    ([17,15,100], [50, 56, 200])
]

# create NumPy arrays from the boundaries
lower = np.array([100,100,200])
upper = np.array([200,200,255])


# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image,lower,upper)
    output = cv2.bitwise_and(image,image,mask = mask)

        
 
    # show the frame
    cv2.imshow("Frame", output)
    key = cv2.waitKey(1) & 0xFF
 
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break



