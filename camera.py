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
EFFECT = "none"

# If directory doesn't exist then this will make it.
# A custom directory path can be input.
def makeDir(dir) :
 if not os.path.exists(dir) :
  os.makedirs(dir)
 fileName = raw_input("What would you like to name your file?\n")
 return "%s/%s" % (dir, fileName)

def printMenu() :
 print("1. Preview\t\t7. Set Brightness 0-100\t13. Set Save Directory (str)\n"+
       "2. Preview Effect\t8. Set Contrast 0-100\t14. Take Picture\n"+
       "3. Preview Contrast\t9. Set Text Size 6-160\t15. Take Pictures (int)\n"+
       "4. Preview Brightness\t10. Set Rotation\t16. Take Recording\n"+
       "5. Print Settings\t11. Set Sleep (int)\t17. Take Picture W/ Caption\n"+
       "6. Set Alpha (int)\t12. Set Effect\t\t0. exit")

# Menu choice logic function
def executeChoice(cam, choice) :
 if choice == 1 :
  cam.takePreview()
 elif choice == 2 :
  cam.previewEffects()
 elif choice == 3 :
  cam.previewContrast()
 elif choice == 4 :
  cam.previewBrightness()
 elif choice == 5 :
  cam.printSettings()
 elif choice == 6 :  
  cam.setAlpha(raw_input("Enter an alpha (default 255): "))
 elif choice == 7 :
  cam.setBrightness(raw_input("Enter Brightness (default 50): "))
 elif choice == 8 :
  cam.setContrast(raw_input("Enter a contrast (default 50): "))
 elif choice == 9 :
  cam.setTextSize(raw_input("Enter a Text size (default 32): "))
 elif choice == 10 :
  cam.setRotation(raw_input("Enter the rotation (default 0): "))
 elif choice == 11 :
  cam.setSleep(raw_input("Enter a sleep length (default 10): "))
 elif choice == 12 :
  print("\nnone, negative, solarize, sketch, denoise, emboss\n"+
        "oilpaint, hatch, gpen, pastel, watercolor, film, blur\n"+
        "saturation, colorswap, washedout, posterise, colorpoint\n"+
        "colorbalance, cartoon, deinterlace1, deinterlace2\n")
  cam.setEffect(raw_input("Set effect: "))
 elif choice == 13 :
  cam.setSaveDir(raw_input("Enter path to save dirctory (default /home/pi/pics): "))
 elif choice == 14 :
  cam.takePicture()
 elif choice == 15 :
  usrIn = raw_input("Enter the number of pictures to take: ")
  cam.takePictures(int(usrIn))
 elif choice == 16 :
  cam.takeRecording()
 elif choice == 17 :
  cam.takePictureWithCaption()
 else :
  print("That is not a valid choice")

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
  self.effect = EFFECT

 def configCamera(self, alphaBool) :
  camera = self.camera
  camera.rotation = self.rotate
  camera.brightness = self.brightness
  camera.contrast = self.contrast
  camera.image_effect = self.effect
  camera.annotate_text_size = self.annotateTextSize
  if alphaBool :
   camera.start_preview()
  else :
   camera.start_preview(alpha=self.alpha)
  return camera

 def printSettings(self) :
  print("\nSleep: %s\tRotation: %s\tAlpha: %s\tEffect: %s" % (self.sleep, self.rotate, self.alpha, self.effect))
  print("Brightness: %s\tContrast: %s\tText Size: %s" % (self.brightness, self.contrast, self.annotateTextSize))
  print("Save Directory: %s\n" % (self.saveDir)) 

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
  self.annotateTextSize = int(size)

 def setEffect(self, effect) :
  self.effect = effect
 
 def getSleep(self) :
  return self.sleep

 def getRotation(self) :
  return self.rotate

 def getAlpha(self) :
  return self.alpha

 def getSaveDir(self) :
  return self.saveDir

 def getBrightness(self) :
  return self.brightness

 def getContrast(self) :
  return self.contrast

 def getTextSize(self) :
  return self.annotateTextSize

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
  camera.annotate_text = ""
  camera.stop_preview()

 def previewBrightness(self) :
  camera = self.configCamera(False)
  for i in range(100) :
   camera.annotate_text = "Brightness: %s" % i
   camera.brightness = i
   if i > 55 :
    camera.annotate_foreground = Color('black')
   sleep(self.sleep)
  camera.annotate_text = ""
  camera.stop_preview()

 def previewContrast(self) :
  camera = self.configCamera(False)
  for i in range(100) :
   camera.annotate_text = "Contrast: %s" % i
   camera.contrast = i
   sleep(self.sleep)
  camera.annotate_text = ""
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
  camera.annotate_text = ""
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
 # create a instance of Picamera an pass it to the PiCam constructor
 camera = PiCamera()
 cam = PiCam(camera)
 # set a default value to start loop
 usrIn = 100
 # create a loop so user can continue to make choices
 while (usrIn > 0) :
  printMenu()
  usrIn = int(raw_input("Enter your choice: "))
  if usrIn > 0 :
   executeChoice(cam, usrIn)
  # clear menu and reprint
  if usrIn != 5 :
   os.system('cls' if os.name == 'nt' else 'clear')

main()