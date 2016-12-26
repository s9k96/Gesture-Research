import cv2
import numpy as np
import math
import os

hand_cascade = cv2.CascadeClassifier('hand.xml')

cap = cv2.VideoCapture(0)

startx, starty = -1, -1
endx, endy = -1, -1
counter = 0
grabbed = False
temperature = 0
diffx = 0
diffy = 0

while cap.isOpened():
    _, frame = cap.read()
    frame1 = frame.copy()
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    hand = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in hand:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        counter = 0
        if startx < 0 and starty < 0:
            startx, starty = x, y

        endx, endy = x, y
    diffx = endx - startx
    diffy = endy - starty
    print   startx, endx, abs(endx-startx)/50
###############################################################################
    if abs(startx-endx)>30:
        diffx=startx-endx
    cv2.putText(frame, str(abs(diffx)/30), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3,(255,0,255),2,cv2.LINE_AA)
    if abs(starty-endy)>30:
        diffy=starty-endy
    cv2.putText(frame, str(abs(endy-starty)/30), (550, 100), cv2.FONT_HERSHEY_SIMPLEX, 3,(255,0,255),2,cv2.LINE_AA)

###################################
    if counter == 5:
    	
        temperature += diffx / 50
###################################
    # print (endx, endy, startx, starty, counter)
    #print ("startx = ", startx, "starty= ", starty)
    counter += 1
    #print (startx, starty)
    if counter > 10:
        startx = -1
        starty = -1
    cv2.imshow('temp', frame)

    k = cv2.waitKey(10)
    if k == 27 & 0xFF:
        break

cap.release()
cv2.destroyAllWindows()
