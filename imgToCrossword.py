#!/usr/bin/python3
# Alexander Hallard - Generate a crossword table from image

import cv2 # Blue Green Red BGR
#import pygame

cap = cv2.VideoCapture(0) #Capture Webcam 0

while(True):
    ret, frame = cap.read() #Read frame

    # edged is the edge detected image
    cnts = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break

    cv2.imshow('frameOriginal', frame) #Show frame in window

    if cv2.waitKey(1) & 0xFF == ord('q'): #Quit on Q
        break

cap.release() #Stop capture
cv2.destroyAllWindows() #Remove windows
