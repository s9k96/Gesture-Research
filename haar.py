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
selected_channel = 0
vertical_slider_value = 0
horizontal_slider_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while cap.isOpened():
    _, frame = cap.read()
    frame1 = frame.copy()
    cv2.putText(frame, str(channel_value), (1, 50), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, str(selected_channel), (1, 100), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, str(horizontal_slider_values[selected_channel]), (1, 150), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 2, cv2.LINE_AA)
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
        channel_value = (y - starty) / 100

    if counter == 5:
        selected_channel += channel_value
    if selected_channel < 1:
        selected_channel = 1
    if selected_channel > 10:
        selected_channel = 10

    if (endx - startx) > 10:
        horizontal_slider_values[selected_channel] = (endx - startx) / 50

    print (endx, endy, startx, starty, counter)
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
