##############################
# Using the PiCamera to record 
# a video sequence
# Author: Lakshmi
###############################

from picamera import PiCamera
from time import sleep

# instantiate the camera
camera = PiCamera()

# Specify the camera resolution
# Note that this directly impacts the capture speed
# 1080p --> 30fps, 720p --> 60fps, vga --> 90fps
camera.resolution = (1920, 1080)
camera.framerate = 30

# Start the recording
camera.start_recording('test_capture2.h264')
camera.wait_recording(120)
camera.stop_recording()
