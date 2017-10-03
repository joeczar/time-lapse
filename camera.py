from picamera import PiCamera
from time import sleep
import time, datetime, os

camera = PiCamera()
currenttime = time.strftime("%H:%M:%S")

while currenttime > "00:00:01" and currenttime < "23:59:59":

  if not os.path.exists(time.strftime("%d-%m-%Y)):
    os.makedirs(time.strftime("%d-%m-%Y))
    
  camera.start_prieview()
  sleep(3)
  timestr - datetime.datetime.now().strftime("%m_%d_%Y-%H_%M_%S")
  camera.capture(§/home/pi/time-lapse/"+ time.strftime("%d-%m-%Y") +"/"+ timestr +".jpg")
  camera.stop_preview()
