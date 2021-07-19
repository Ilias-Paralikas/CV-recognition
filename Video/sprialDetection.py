from typing import OrderedDict
import cv2
import numpy as np
from math import cos, sin
import os

originalImg = cv2.imread('rescourses/plaketa.jpg', 0)
if originalImg.size ==0:
    print('image is empty')
    quit()
imgHegith, imgWidth = originalImg.shape
imgCentr = (imgHegith//2, imgWidth//2)



frameHeight = 100
frameWidth = 200
frameCenter = imgCentr

#read the templates from a file all the templates in a Dict so we can can call  them by their name
templateFolder= 'rescourses/templates'
templateDict = {}
for filename in os.listdir(templateFolder):
    template =  cv2.imread(templateFolder + '/'+filename, 0)
    name = filename.split('.')[0]
    templateDict[name] = template
    if(template.shape[0] > frameHeight or template.shape[1]>frameWidth ):
        print('Template needs to fit in the frame, but has bigger dimentions')
        quit() 

if not templateDict:
    print('template dict is empty, make sure the files are correct')
    quit()




spiralCentrer = imgCentr


def cyclicalToCartesian(range, angle): return (int(range * cos(angle) + spiralCentrer[0]),
                                               int(range * sin(angle)+spiralCentrer[1]))


range = 0
angle = 0
threshold = 0.95

ANIMATION = int(input('enter 1 to turn on ANIMATION, 0 to turn off : '))
while ANIMATION  != 0 and ANIMATION != 1 :
    ANIMATION = int(input('enter 1 to turn on ANIMATION, 0 to turn off : '))
ANIMATION = bool(ANIMATION)

while True:
    if ANIMATION:
        imgCopy = originalImg.copy()
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
    frame = originalImg[lowerHeightBound:upperHeightBound,
                lowerWidthBound:upperWidthBound]

    if ANIMATION:
        cv2.rectangle(imgCopy,(lowerWidthBound,lowerHeightBound),(upperWidthBound,upperHeightBound),255,5)
        cv2.imshow('ANIAMATION',imgCopy)
        cv2.waitKey(5)


    for key in templateDict:
        template = templateDict[key]

        result = cv2.matchTemplate(frame,template, cv2.TM_CCORR_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if(max_val > threshold):
            cv2.rectangle(frame,max_loc, (max_loc[0]+template.shape[1], max_loc[1]+template.shape[0]),255,5)
            del templateDict[key]
            break

