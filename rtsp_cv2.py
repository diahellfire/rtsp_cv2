import face_recognition
import cv2
import numpy as np
from goto import goto, label
from os import system, name
import random
import string

def randomString(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


# Get a reference to webcam #0 (the default one)
#video_capture = cv2.VideoCapture(0)

system('clear')

array = dict()

array['url']="rtsp://10.15.44.14:554/user=admin&password=PASSWORD&channel=1&stream=0?.sdp"
array['errors']=0
array['frames']=0
array['detected']=0
array['last']='Not identifyed'
label .label

print("Connecting to: " + array['url'] + " ... ")

video_capture = cv2.VideoCapture(array['url'])

while True:

    if (video_capture.isOpened()== False):
     print("Error opening video")
     array['errors']=array['errors']+1;
     goto .label;

    array['w']=video_capture.get(3)
    array['h']=video_capture.get(4)
    array['fps']=video_capture.get(5)

    ret, frame = video_capture.read()

    if (ret==False):
     print("Error reading frame")
     array['errors']=array['errors']+1;
     goto .label;

    #rgb_frame = frame[:, :, ::-1]
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    array['frames']=array['frames']+1;

    face_locations = face_recognition.face_locations(rgb_frame)

    # Loop through each face in this frame of video
    for face_location in face_locations:
      top, right, bottom, left = face_location
      array['detected']=array['detected']+1
      array['last']=("located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
      cv2.imwrite("/data/detected/" + str(randomString()) + "_thumb_rtsp.jpg", frame)

    system('clear')
    print("===================================================================================")
    print("RTSP NN Detected --- Version 0.15 --- S-SG TechLab by S-SG LLC")
    print("===================================================================================")
    print("RTSP stream URL: " + array['url'])
    print("Scanning frames: " + str(array['frames']))
    print("Detected faces: " + str(array['detected']))
    print("Detected faces location: " + str(array['detected']))
    print("Errors: " + str(array['errors']))
    print("Stream details (Frame size: " + str(array['w']) + "x" + str(array['h']) + " FPS: " + str(array['fps']))
    print("===================================================================================")

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
