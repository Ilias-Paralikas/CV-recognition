from typing import OrderedDict
import cv2
import numpy as np
from math import cos, sin


img = cv2.imread('plaketa.jpg', 0)
imgHegith, imgWidth = img.shape
imgCentr = (imgHegith//2, imgWidth//2)

template = cv2.imread('template.jpg',0)
templateHeight,templateWidth = template.shape


frameHeight = 100
frameWidth = 200
frameCenter = imgCentr

spiralCentrer = imgCentr



if(template.shape[0] > frameHeight or template.shape[1]>frameWidth ):
    print('Template needs to fit in the frame, but has bigger dimentions')
    quit()  

def cyclicalToCartesian(range, angle): return (int(range * cos(angle) + spiralCentrer[0]),
                                               int(range * sin(angle)+spiralCentrer[1]))


range = 0
angle = 0
threshold = 0.95
while True:
    range = range+1
    angle = angle + 0.08
    frameCenter = cyclicalToCartesian(range, angle)

    lowerHeightBound = frameCenter[0]-frameHeight//2
    upperHeightBound = frameCenter[0]+frameHeight//2
    lowerWidthBound = frameCenter[1]-frameWidth//2
    upperWidthBound = frameCenter[1]+frameWidth//2

    if lowerHeightBound < 0 or upperHeightBound > imgHegith or lowerWidthBound < 0 or upperWidthBound > imgWidth:
        print("frame is out of bounds")
        break
    frame = img[lowerHeightBound:upperHeightBound,
                lowerWidthBound:upperWidthBound]

    result = cv2.matchTemplate(img,template, cv2.TM_CCORR_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    if(max_val > threshold):
        location = max_loc


    if cv2.waitKey(1) == ord('q'):
        break

cv2.rectangle(img,location, (location[0]+templateWidth, location[1]+templateHeight),(255,0,0),10)

cv2.imshow("method " +str(max_val),img)
cv2.waitKey(0)
cv2.destroyAllWindows()
