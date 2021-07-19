from typing import OrderedDict
import cv2
import numpy as np
from math import cos, sin
import os

img = cv2.imread('plaketa.jpg', 0)
imgHegith, imgWidth = img.shape
imgCentr = (imgHegith//2, imgWidth//2)



frameHeight = 100
frameWidth = 200
frameCenter = imgCentr

#read the templates from a file all the templates in a Dict so we can can call  them by their name
templateFolder= 'templates'
templateDict = {}
for filename in os.listdir(templateFolder):
    template =  cv2.imread(templateFolder + '/'+filename, 0)
    name = filename.split('.')[0]
    templateDict[name] = template
    if(template.shape[0] > frameHeight or template.shape[1]>frameWidth ):
        print('Template needs to fit in the frame, but has bigger dimentions')
        quit() 

spiralCentrer = imgCentr


 

def cyclicalToCartesian(range, angle): return (int(range * cos(angle) + spiralCentrer[0]),
                                               int(range * sin(angle)+spiralCentrer[1]))


range = 0
angle = 0
threshold = 0.95
templateFound = False
while not templateFound:
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

    for key in templateDict:
        template = templateDict[key]

        result = cv2.matchTemplate(img,template, cv2.TM_CCORR_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if(max_val > threshold):
            cv2.rectangle(img,max_loc, (max_loc[0]+template.shape[1], max_loc[1]+template.shape[1]),(255,0,0),10)
            cv2.imshow("method " +str(max_val),img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            templateFound = True

