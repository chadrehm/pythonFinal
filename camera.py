#!/usr/bin/env python
# program name: PiCam
# name: Chad Rehm
# date: 8/9/17
# This program create an easy interface to pic camera functions.

from picamera import PiCamera, Color
from time import sleep
import os

# constance
SLEEP = 10
ROTATE = 0
ALPHA = 255
DEFULT_SAVE_DIR = "/home/pi/pics"
BRIGHTNESS = 50
CONTRAST = 50
ANNOTATE_TEXT_SIZE = 32

def makeDir(dir) :
 if not os.path.exists(dir) :
  os.makedirs(dir)
 fileName = raw_input("What would you like to name your file?\n")
 return "%s/%s" % (dir, fileName)

def executeChoice(cam, choice) :
 if choice == 1 :
  cam.takePreview()
 elif choice == 2 :
  cam.previewEffects
 elif choice == 3 :
  cam.previewContrast()
 elif choice == 4 :
  cam.previewBrightness()
 elif choice == 5 :
  cam.setAlpha(raw_input("Enter an alpha: "))
 elif choice == 6 :
  cam.setBrightness(raw_input("Enter Brightness: "))
 elif choice == 9 :
  cam.setRotation(raw_input("Enter the rotation: "))
 elif choice == 10 :
  cam.setContrast(raw_input("Enter a contrast: "))
 elif choice == 13 :
  cam.setSleep(raw_input("Enter sleep length: "))

class PiCam :
 def __init__(self, camera) :
  self.camera = camera
  self.rotate = ROTATE
  self.alpha = ALPHA
  self.saveDir = DEFULT_SAVE_DIR
  self.sleep = SLEEP
  self.brightness = BRIGHTNESS  
  self.contrast = CONTRAST
  self.annotateTextSize = ANNOTATE_TEXT_SIZE

 def configCamera(self, alphaBool) :
  camera = self.camera
  camera.rotation = self.rotate
  camera.brightness = self.brightness
  camera.annotate_text_size = self.annotateTextSize
  if alphaBool :
   camera.start_preview()
  else :
   camera.start_preview(alpha=self.alpha)
  return camera

 def setSleep(self, sleep) :
  self.sleep = float(sleep)

 def setRotation(self, rotate) :
  self.rotate = int(rotate)

 def setAlpha(self, alpha) :
  self.alpha = int(alpha)

 def setSaveDir(self, dir) :
  self.saveDir = dir

 def setBrightness(self, brightness) :
  self.brightness = int(brightness)

 def setContrast(self, contrast) :
  self.contrast = int(contrast)

 def setTextSize(self, size) :
  self.annotateTextSize = size

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
   if i > 65 :
    camera.annotate_foreground = Color('black')
   sleep(self.sleep)
  camera.stop_preview()

 def previewContrast(self) :
  camera = self.configCamera(False)
  for i in range(100) :
   camera.annotate_text = "Contrast: %s" % i
   camera.contrast = i
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
  caption = raw_input("What caption should I add?\n")
  camera = self.configCamera(True)
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
 camera = PiCamera()
 cam = PiCam(camera)
 print("1. Preview\t\t6. Set Brightness 0-100\t11. Set Save Directory (str)\n"+
       "2. Preview Effect\t7. Set Contrast 0-100\t12. Take Picture\n"+
       "3. Preview Contrast\t8. Set Text Size 6-160\t13. Take Pictures (int)\n"+
       "4. Preview Brightness\t9. Set Rotation\t\t14. Take Recording\n"+
       "5. Set Alpha (int)\t10. Set Sleep (int)\t15. Take Picture W/ Caption\n"+
       "0. exit")
 usrIn = 100
 while (usrIn > 0) :
  usrIn = int(raw_input("Enter your choice: "))
  if usrIn > 0 :
   executeChoice(cam, usrIn)

main()