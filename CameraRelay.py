#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import cv2 as cv
import argparse
import os
import signal
import sys

RELAY_PIN = 11
RELAY_MODE_HIGH = 0
RELAY_MODE_LOW = 1
RELAY_MODE = RELAY_MODE_HIGH

OPENCV_VIDEO_SRC = 0
IMAGE_DIR = "image"

# SYSTEM_DEBUG = True
SYSTEM_DEBUG = True

class CameraRelay:
	powerOnTime = 0
	powerOffTime = 0
	cameraCaptureDelay = 0

	def __str__(self):
		return " \
powerOnTime: {}.\n\r \
powerOffTime: {}.\n\r \
cameraCaptureDelay: {}.\n\r \
" .format(\
self.powerOnTime, \
self.powerOffTime, \
self.cameraCaptureDelay \
)

context = CameraRelay()

def DEBUG(mesg):
	if SYSTEM_DEBUG :
		print(mesg)

def signal_handler(signal, frame):
	system_exit('\r\nCtrl+c With Bye Bye!')

def system_exit(mesg):
	GPIO.cleanup()
	print(mesg)
	sys.exit(0)

def setUpRelayWithDefault(pin, value):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, value)

	return


# @mode:
#   0: Active low(RELAY_MODE_HIGH = 0)
#   1: Active high(RELAY_MODE_LOW = 1)
def setRelayAction(pin, mode, pulseTime):
	if mode == 0:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(pin, GPIO.LOW)
		time.sleep(pulseTime)
		GPIO.output(pin, GPIO.HIGH)
	else:
		GPIO.output(pin, GPIO.LOW)
		time.sleep(0.1)
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(pulseTime)
		GPIO.output(pin, GPIO.LOW)



def setUPCamera():
	try: 
		camera = cv.VideoCapture(OPENCV_VIDEO_SRC)
	except:
		system_exit("Please Check Your Ready.\r\n")
	
	return camera


def cameraCapture(camera):
	ret, img = camera.read()
	
	return img

def cameraCaptureAndSave(camera, fileName):
	img = cameraCapture(camera)
	
	# Save the result image
	cv.imwrite('image/' + fileName + '.jpg', img)


def getDateString():
	return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))


if __name__ == '__main__':

	signal.signal(signal.SIGINT, signal_handler)

	parser = argparse.ArgumentParser(
		description='Camera Control Relay.',
		epilog="Example: ./CameraRelay.py -on 4 -off 2 -cap 1 ")
	parser.add_argument('-on', required=True, help='Power On Duty(s)')
	parser.add_argument('-off', required=True, help='Power Off Duty(s)')
	parser.add_argument('-cap', required=True, help='Camera Capture Image Delay After Power On(s)')
	
	# Parse argument
	args = parser.parse_args()
	print(args)

	# save arguments to context
	context.powerOnTime = float(args.on)
	context.powerOffTime = float(args.off)
	context.cameraCaptureDelay = float(args.cap)
	DEBUG(context)

	if not os.path.exists(IMAGE_DIR):
		os.makedirs(IMAGE_DIR)

	# init gpio and camera
	setUpRelayWithDefault(RELAY_PIN, GPIO.HIGH if RELAY_MODE == RELAY_MODE_HIGH else GPIO.LOW)
	camera = setUPCamera()

	print("Program Is Running...")
	print("Type Ctrl+c to stop the program.")

	count = 0
	while True:
		DEBUG("start power off: {}".format(getDateString()))
		setRelayAction(RELAY_PIN, RELAY_MODE, context.powerOffTime)
		DEBUG("over power off and start power on: {}".format(getDateString()))
		time.sleep(context.cameraCaptureDelay)
		DEBUG("capture a image: {}".format(getDateString()))
		cameraCaptureAndSave(camera, getDateString())
		time.sleep(context.powerOnTime - context.cameraCaptureDelay)
		DEBUG("over power on: {}".format(getDateString()))
		
		count += 1
		DEBUG("Capture image count: {}".format(count))

