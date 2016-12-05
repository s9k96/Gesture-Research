import cv2
import numpy as np

hand_cascade = cv2.CascadeClassifier('hand.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hand = hand_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in hand:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('temp', frame)
    k = cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()