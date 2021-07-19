from typing import OrderedDict
import cv2
import numpy as np
from math import cos, sin
import os

img = cv2.imread('rescourses/plaketa.jpg', 0)
imgHegith, imgWidth = img.shape
imgCentr = (imgHegith//2, imgWidth//2)


frameHeight = 200
frameWidth = 200
frameCenter = imgCentr

# read the templates from a file all the templates in a Dict so we can can call  them by their name
templateFolder = 'rescourses/templates'
templateDict = {}
for filename in os.listdir(templateFolder):
    template = cv2.imread(templateFolder + '/'+filename, 0)
    name = filename.split('.')[0]
    templateDict[name] = template
    if(template.shape[0] > frameHeight or template.shape[1] > frameWidth):
        print('Template needs to fit in the frame, but has bigger dimentions')
        quit()



print('press \'w\',\'a\',\'s\',\'d\' to move around and \'q\'  to exit \npress ENTER to continue')
input()
threshold = 0.95
while True:

    tempImg = img.copy()

    lowerHeightBound = frameCenter[0]-frameHeight//2
    upperHeightBound = frameCenter[0]+frameHeight//2
    lowerWidthBound = frameCenter[1]-frameWidth//2
    upperWidthBound = frameCenter[1]+frameWidth//2

    if lowerHeightBound < 0 or upperHeightBound > imgHegith or lowerWidthBound < 0 or upperWidthBound > imgWidth:
        print("frame is out of bounds")
        print(lowerHeightBound, lowerWidthBound,
              upperHeightBound, upperWidthBound)
        print(0, 0, imgHegith, imgWidth)

        break
    frame = img[lowerHeightBound:upperHeightBound,
                lowerWidthBound:upperWidthBound]

    cv2.rectangle(tempImg, (lowerWidthBound, lowerHeightBound),
                  (upperWidthBound, upperHeightBound), 0, 0)
    cv2.imshow('plaketa', tempImg)

    button = cv2.waitKey(1)
    # DOWN
    if button == ord('s') or button == ord('S'):
        frameCenter = (frameCenter[0]+2, frameCenter[1])
    # UP
    if button == ord('w') or button == ord('W'):
        frameCenter = (frameCenter[0]-2, frameCenter[1])
    # LEFT
    if button == ord('a') or button == ord('A'):
        frameCenter = (frameCenter[0], frameCenter[1]-2)
    # RIGHT
    if button == ord('d') or button == ord('D'):
        frameCenter = (frameCenter[0], frameCenter[1]+2)

    for key in templateDict:
        template = templateDict[key]

        result = cv2.matchTemplate(frame, template, cv2.TM_CCORR_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if(max_val > threshold):
            cv2.rectangle(
                frame, max_loc, (max_loc[0]+template.shape[1], max_loc[1]+template.shape[1]), (255, 0, 0), 10)

    if button == ord('q') or button == ord('Q'):
        break


cv2.destroyAllWindows()
