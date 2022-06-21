#!/usr/bin/python3
import cv2
import numpy as np
from time import sleep

#img = cv2.imread("crossword.jpg")

cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    # convert to Grayscale
    grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    (thresh, junk) = cv2.threshold(grayScale, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow("grayScale", cv2.resize(grayScale,(720,1280)))

    # get external contours
    contours = cv2.findContours(junk, cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    result1 = img.copy()
    for c in contours:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            cv2.drawContours(result1,[c],0,(0,255,0),2)

    # display result
    #
    cv2.imshow("junk", cv2.resize(junk,(720,1280)))
    cv2.imshow("result", cv2.resize(result1,(720,1280)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.waitKey(0)
cv2.destroyAllWindows()
