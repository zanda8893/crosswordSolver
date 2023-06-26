#!/usr/bin/python3
# pylint: disable=no-member
from time import sleep
import cv2
import numpy as np
from shapely.geometry import Polygon


#img = cv2.imread("crossword.jpg")

cap = cv2.VideoCapture(0)

#shape = np.zeros((100,100,3), dtype=np.uint8)

#cv2.rectangle(shape, (5, 5),(5, 5), (0, 128, 255), -1)

while True:
    ret, img = cap.read()
    # convert to Grayscale
    grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    (thresh, junk) = cv2.threshold(grayScale, 127, 255, cv2.THRESH_BINARY)

    #blur  = cv2.GaussianBlur(img, (5,5),cv2.BORDER_DEFAULT)
    #cv2.addWeighted(blur, 1.5, img, -0.5, 0, img)

    #cv2.imshow("grayScale", cv2.resize(grayScale,(720,1280)))

    filter2D = cv2.filter2D(junk, -1, np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]))
    #cv2.imshow("2D Filter", cv2.resize(junk,(720,1280)))

    # get external contours
    contours = cv2.findContours(filter2D, cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    result1 = img.copy()

    for c in contours:
        #pgon = Polygon(zip(c[0][0][0], y))
        approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)

        if len(approx) >= 4 and len(approx) <= 12:
            centroid = c.mean(axis=0)
            if (c[0][0][0] - centroid[0]) > 50:
                cv2.drawContours(result1,[c],0,(0,255,0),2)
                print(c[0][0][0] - centroid)
                cv2.drawContours(result1,np.array(centroid).reshape((-1,1,2)).astype(np.int32),0,(255,0,0),2)
                #print (int(filter2D[centroid]))
                #print(len(approx))


    # display result
    #
    #cv2.imshow("junk", cv2.resize(junk,(720,1280)))
    cv2.imshow("result", cv2.resize(result1,(720,1280)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('p'):
        sleep(10)

"""
print(type(contours[0]))
for c in contours:
    if len(c[0]) <= 4: # Example [[[ 69,478]],[[ 70,477]],[[ 71,478]],[[ 70,479]]]
        for xy in c[0]:

            if (xy[0][0] + xy [0][1] )


print(contours[0], "\n\n")
print(contours[0][0], "\n\n")
print(contours[0][0][0], "\n\n")
print(contours[0][0][0][0])
"""

cv2.waitKey(0)
cv2.destroyAllWindows()
