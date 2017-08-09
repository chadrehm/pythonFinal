#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
import os

# constance
SLEEP = 10
ROTATE = 0
ALPHA = 255

class PiCam :
 def __init__(self) :
  self.rotate = ROTATE
  self.alpha = ALPHA
  self.saveDir = "/home/pi/pics"

 def setRotation(self, rotate) :
  self.rotate = rotate

 def setAlpha(self, alpha) :
  self.alpha = alpha

 def setSaveDir(self, dir) :
  self.saveDir = dir

 def takePreview(self) :
  camera = PiCamera()
  camera.rotation = self.rotate
  camera.start_preview(alpha=self.alpha)
  sleep(SLEEP)
  camera.stop_preview()

 def takePicture(self) :
  if not os.path.exists(self.saveDir) :
   os.makedirs(self.saveDir)
  fileName = raw_input("what would you like to name your picture?\n")
  savePath = "%s/%s.jpg" % (self.saveDir, fileName)
  camera = PiCamera()
  camera.rotation = self.rotate
  camera.start_preview()
  sleep(SLEEP)
  camera.capture(savePath)
  camera.stop_preview()

 def takePictures(self, numPics) :
  if not os.path.exists(self.saveDir) :
   os.makedirs(self.saveDir)
  fileName = raw_input("what would you like to name your picture?\n")
  savePath = "%s/%s" % (self.saveDir, fileName)
  camera = PiCamera()
  camera.rotation = self.rotate
  camera.start_preview()
  sleep(SLEEP)
  for i in range(numPics) :
   sleep(1)
   print('%s%s.jpg' % (savePath,i))
   camera.capture('%s%s.jpg' % (savePath,i))
  camera.stop_preview()
 

def main() :
 cam = PiCam()
 cam.setRotation(270)
 cam.setSaveDir("/home/pi/pics2")
 cam.takePictures(5)

main()