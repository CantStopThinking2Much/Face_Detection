import os
import time
from datetime import datetime
from playsound3 import playsound  # to play wav and mp3 format audio files
import pyttsx3  # supports native text to speech libraries on windows, reads texts directly from the program 
import cv2 as cv
from path import Path

# Python program that disables the sentry gun's firing mechanism when it detects human faces in an image

engine = pyttsx3.init()
engine.setProperty('rate', 145)
engine.setProperty('volume', 1.0)

root_dir = os.path.abspath('./')
gunfire_path = os.path.join(root_dir, 'gunfire.wav')
tone_path = os.path.join(root_dir, 'tone.wav')

# If any problems arise check the path below
path = Path.path
face_cascade = cv.CascadeClassifier(path + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(path + 'haarcascade_eye.xml')

os.chdir('Face_Detection/Faces')
contents = sorted(os.listdir())
print(contents)

for image in contents:
    print(f"\nMotion detected....{datetime.now()}")
    discharge_weapon = True

    engine.say("You have entered active firezone. \
               Stop and face the gun immediately. \
               When you hear the tone, you have 5 seconds to pass.")
    engine.runAndWait()
    time.sleep(3)

    img_gray = cv.imread(image, cv.IMREAD_GRAYSCALE)
    height, width = img_gray.shape
    cv.imshow(f"Motion detected {image}", img_gray)
    cv.waitKey(2000)
    cv.destroyWindow('Motion detected {image}')