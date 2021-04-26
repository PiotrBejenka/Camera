import datetime
import time
import os
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False);

GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)

camera = PiCamera()
camera.rotation =180
camera.resolution = (1920, 1080)
camera.framerate = 30
camera.start_preview()

def PHOTO():
	photo_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
	camera.capture(str(photo_name) + '.jpg')

def VIDEO():
	video_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
	camera.start_recording(str(video_name) + '.h264')
	while GPIO.input(27) == True:
		time.sleep(.001)
	camera.stop_recording()
	CONVERSION(video_name)

def CONVERSION(video_name):
	os.system("MP4Box -add " + video_name + ".h264 " + video_name + ".mp4")
	os.remove(video_name + ".h264")

while True:
	make_video = GPIO.input(17)
	make_photo = GPIO.input(24)

	if make_video == False:
		VIDEO()

	if make_photo == False:
		PHOTO()
