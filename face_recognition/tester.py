#  This line of codes is from a practice session code from a youtube tutorial
#  Face Recognition with OpenCV in Python Tutorial |Face detection  by Neha Yadav
#  link:- https://www.youtube.com/watch?v=h21wMKGs0qs&t=1046s
#  It may seem like a copy paste codes if you look at the youtube tutorial 
#  yes,this is my first steps towards python programming on OpenCV which I could sucessfully execute
#  growing don't stops here tho.

import cv2 
import os 
import numpy as np 
import face_detection as fd

test_img=cv2.imread('james.JPG')
faces_detected,gray_img=fd.faceDetection(test_img)
print("faces Detected:",faces_detected)

for(x,y,w,h) in faces_detected:
    print(x,y,w,h)
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)

resized_img=cv2.resize(test_img,(600,500))
cv2.imshow("face Detection tutorial",resized_img)

cv2.waitKey(0)

cv2.destroyAllWindows