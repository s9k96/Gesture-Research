import cv2
import numpy as np
import math

hand_cascade = cv2.CascadeClassifier('hand.xml')

cap = cv2.VideoCapture(0)

startx, starty = -1, -1
counter = 0

while cap.isOpened():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    hand = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in hand:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        counter = 0
        if startx < 0 and starty < 0 and counter == 0:
            startx, starty = x,y
        if startx != -1 and starty != -1:
            print ((math.fabs(x - startx),math.fabs(y - starty)))

    print ("startx = ", startx, "starty= ", starty)
    counter = counter + 1
    #print (startx, starty)
    if counter > 10:
        startx = -1
        starty = -1
    cv2.imshow('temp', frame)
    k = cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
