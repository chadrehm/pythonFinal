#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
import os

# constance
SLEEP = 10
ROTATE = 0
ALPHA = 255
DEFULT_SAVE_DIR = "/home/pi/pics"

def makeDir(dir) :
 if not os.path.exists(dir) :
  os.makedirs(dir)
 fileName = raw_input("What would you like to name your file?\n")
 return "%s/%s" % (dir, fileName)

class PiCam :
 def __init__(self) :
  self.rotate = ROTATE
  self.alpha = ALPHA
  self.saveDir = DEFULT_SAVE_DIR
  self.sleep = SLEEP

 def configCamera(self, alphaBool) :
  camera = PiCamera()
  camera.rotation = self.rotate
  if alphaBool :
   camera.start_preview()
  else :
   camera.start_preview(alpha=self.alpha)
  return camera

 def setSleep(self, sleep) :
  self.sleep = sleep

 def setRotation(self, rotate) :
  self.rotate = rotate

 def setAlpha(self, alpha) :
  self.alpha = alpha

 def setSaveDir(self, dir) :
  self.saveDir = dir

 def takePreview(self) :
  camera = self.configCamera(False)
  sleep(self.sleep)
  camera.stop_preview()

 def previewEffects(self) :
  camera = self.configCamera(False)
  for effect in camera.IMAGE_EFFECTS :
   camera.image_effect = effect
   camera.annotate_text = "Effect: %s" % effect
   sleep(self.sleep)
  camera.stop_preview()

 def previewBrightness(self) :
  camera = self.configCamera(False)
  for i in range(100) :
   camera.annotate_text = "Brightness: %s" % i
   camera.brightness = i
   sleep(self.sleep)
  camera.stop_preview()

 def takePicture(self) :
  savePath = makeDir(self.saveDir) 
  camera = self.configCamera(True)
  sleep(self.sleep)
  camera.capture('%s.jpg' % savePath)
  camera.stop_preview()

 def takePictureWithCaption(self) :
  savePath = makeDir(self.saveDir) 
  camera = self.configCamera(True)
  caption = raw_input("What caption should I add?\n")
  camera.annotate_text = caption
  sleep(self.sleep)
  camera.capture('%s.jpg' % savePath)
  camera.stop_preview()

 def takePictures(self, numPics) :
  savePath = makeDir(self.saveDir)
  camera = self.configCamera(True)
  sleep(self.sleep)
  for i in range(numPics) :
   sleep(1)
   camera.capture('%s%s.jpg' % (savePath,i))
  camera.stop_preview()

 def takeRecording(self) :
  savePath = makeDir(self.saveDir)
  camera = self.configCamera(True)
  camera.start_recording('%s.h264' % savePath)
  sleep(self.sleep)
  camera.stop_recording()
  camera.stop_preview()

def main() :
 cam = PiCam()
 cam.setRotation(270)
 cam.setSleep(10)
 cam.setAlpha(200)
 cam.setSaveDir("/home/pi/pics2")
 cam.takePictureWithCaption()

main()