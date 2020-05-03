#  This line of codes is from a practice session code from a youtube tutorial
#  Face Recognition with OpenCV in Python Tutorial |Face detection  by Neha Yadav
#  link:- https://www.youtube.com/watch?v=h21wMKGs0qs&t=1046s
#  It may seem like a copy paste codes if you look at the youtube tutorial 
#  yes,this is my first steps towards python programming on OpenCV which I could sucessfully execute
#  growing don't stops here tho.




import cv2 
import os 
import numpy as np

def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    face_haar_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml') #here the complete path should be defined
    faces=face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32, minNeighbors=5)
    return faces,gray_img