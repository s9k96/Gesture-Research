import cv2
import numpy as np
from  matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
roi = cv2.imread('hand-01.jpg')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
fgbg = cv2.createBackgroundSubtractorKNN()
kernel = np.ones((5,5),np.uint8)


while cap.isOpened():
    _, frame = cap.read()

    fgmask = fgbg.apply(frame)
    temp = cv2.bitwise_and(frame, frame, mask=fgmask)
    cv2.imshow('frame', temp)
    hsvt = cv2.cvtColor(temp, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)
    #cv2.filter2D(dst, -1, disc, dst)
    #cv2.imshow('frame', dst)
    ret, thresh = cv2.threshold(dst, 50, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    dilation = cv2.dilate(thresh, kernel, iterations=1)
    #cv2.imshow('frame', thresh)
    #thresh = cv2.merge((thresh, thresh, thresh))
    #res = cv2.bitwise_and(frame, thresh)
    cv2.imshow('temp', dilation)


    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()