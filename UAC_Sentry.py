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

path = Path.path
face_cascade = cv.CascadeClassifier(path + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(path + 'haarcascade_eye.xml')


os.chdir('Real_World_Py\\Faces')
contents = sorted(os.listdir())

for image in contents:
    print(f"\nMotion detected....{datetime.now()}")
    discharge_weapon = True
    
   
    img_gray = cv.imread(image, cv.IMREAD_GRAYSCALE)
    height, width = img_gray.shape
    cv.imshow(f"Motion detected {image}", img_gray)
    cv.waitKey(1000)
    
    # Use the pttysx3 engine object's say() to speak. It takes texts as argument.
    engine.say("You have entered active firezone. \
               Stop and face the gun immediately. \
               When you hear the tone, you have 5 seconds to pass.")
    engine.runAndWait()
    time.sleep(3)

    cv.waitKey(2000)
    cv.destroyWindow(f"Motion detected {image}")

    face_rect_list = [] 
    face_rect_list.append(face_cascade.detectMultiScale(image=img_gray,
                                                        scaleFactor=1.1,
                                                        minNeighbors=5))