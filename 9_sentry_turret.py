import os
import time
from datetime import datetime
from playsound3 import playsound
import pyttsx3
import cv2 as cv
from path import Path

# Pythonpy program that disables the sentry gun's firing mechanism when it detects human faces in an image

engine = pyttsx3.init()
engine.setProperty('rate', 145)
engine.setProperty('volume', 1.0)

root_dir = os.path.abspath('./')
gunfire_path = os.path.join(root_dir, 'gunfire.wav')
tone_path = os.path.join(root_dir, 'tone.wav')

# If any problems arise check the path below
# TODO find haarcascade_frontalface_default and haarcascade_eye.xml in C:/ directory
path = Path.path
face_cascade = cv.CascadeClassifier(path + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(path + 'haarcascade_eye.xml')

os.chdir('Faces')
contents = sorted(os.listdir())