#! /usr/bin/env python3

# Copyright(c) 2017 Intel Corporation. 
# License: MIT See LICENSE file in root directory. 

# Modified to include live demo
# Author: Lakshmi


from mvnc import mvncapi as mvnc
from picamera.array import PiRGBArray
from picamera import PiCamera
import sys
import numpy
import cv2
import time
import csv
import os
import sys

def init_graph(blob):
	mvnc.SetGlobalOption(mvnc.GlobalOption.LOG_LEVEL, 2)
	devices = mvnc.EnumerateDevices()
	if len(devices) == 0:
		print('No devices found')
		quit()
	device = mvnc.Device(devices[0])
	device.OpenDevice()
	opt = device.GetDeviceOption(mvnc.DeviceOption.OPTIMISATION_LIST)
	with open(blob, mode='rb') as f:
		blob = f.read()
	graph = device.AllocateGraph(blob)
	graph.SetGraphOption(mvnc.GraphOption.ITERATIONS, 1)
	iterations = graph.GetGraphOption(mvnc.GraphOption.ITERATIONS)
	return graph, device

def execute_graph(graph,img):
	graph.LoadTensor(img.astype(numpy.float16), 'user object')
	output, userobj = graph.GetResult()
	return output,userobj

# open the network blob files
blob='agenet.graph'

# categories for age and gender
age_list=['0-2','4-6','8-12','15-20','25-32','38-43','48-53','60-100']
gender_list=['Male','Female']

# input shape for the network
dim=(227,227)

# create a camera instance with specified parameters
# here we opt for a lower resolution since the network was trained on a much smaller dimnesion
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 90
raw_image = PiRGBArray(camera,size=(640, 480))

# to avoid the initial burst of exposure
time.sleep(0.1)

# initialize the graph on movidius
graph, device = init_graph(blob)

# start capturing
for frame in camera.capture_continuous(raw_image, format="bgr", use_video_port=True):
	img = frame.array
	cv2.imshow("Live Feed", img)
	key = cv2.waitKey(1) & 0xFF
	raw_image.truncate(0)

	img=cv2.resize(img,dim)
	# mean subtract
	img = img.astype(numpy.float32)
	img[:,:,0] = (img[:,:,0] - 127.0) 
	img[:,:,1] = (img[:,:,1] - 127.0)
	img[:,:,2] = (img[:,:,2] - 127.0)

	#execute the network with the input image on the NCS
	output,userobj=execute_graph(graph,img)
	print('\n------- predictions --------')
	order = output.argsort()
	last = len(order)-1
	predicted=int(order[last])
	#print('the predicted gender is ' + gender_list[predicted] + ' with confidence of %3.1f%%' % (100.0*output[predicted]))
	print('the age range is ' + age_list[predicted] + ' with confidence of %3.1f%%' % (100.0*output[predicted]))

	if key == ord("q"):
		break

# deallocate memory and quit
graph.DeallocateGraph()
device.CloseDevice()
