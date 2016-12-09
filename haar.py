import cv2
import numpy as np
import math

hand_cascade = cv2.CascadeClassifier('hand.xml')

cap = cv2.VideoCapture(0)

startx, starty = -1, -1
endx, endy = -1, -1
counter = 0
grabbed = False
channel_value = 0
vertical_slider_value = 0

while cap.isOpened():
    _, frame = cap.read()
    frame1 = frame.copy()
    cv2.putText(frame, str(channel_value), (1, 50), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, str(vertical_slider_value), (1, 100), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 2, cv2.LINE_AA)
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    hand = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in hand:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        counter = 0
        if startx < 0 and starty < 0:
            startx, starty = x, y

        endx, endy = x, y

        if startx > 0:
            temp = y - starty
            if temp > 0:
                temp %= 200
                channel_value -= 1
            else:
                temp %= 200
                channel_value += 1
            if channel_value < 0:
                channel_value = 0
            if channel_value > 20:
                channel_value = 20

    print (endx, endy, startx, starty, counter)
    #print ("startx = ", startx, "starty= ", starty)
    counter += 1
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
