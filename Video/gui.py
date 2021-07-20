from typing import OrderedDict
import cv2
import numpy as np
from math import cos, sin
import os

img = cv2.imread('rescourses/plaketa.jpg', 0)
imgHeigth, imgWidth = img.shape

frameHeight = 200
frameWidth = 200
frameCenter = (imgHeigth//2, imgWidth//2)

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


def zoom(zoomFactor, img, templateDict, frameWidth, frameHeight, frameCenter):
    img = cv2.resize(img, (0, 0), fx=zoomFactor, fy=zoomFactor)
    imgHeigth, imgWidth = img.shape
    

    frameWidth = int(frameWidth * zoomFactor)
    frameHeight = int(frameHeight * zoomFactor)
    frameCenter = (int(frameCenter[0] * zoomFactor),
                   int(frameCenter[1] * zoomFactor))
    for key in templateDict:
        templateDict[key] = cv2.resize(
            templateDict[key], (0, 0), fx=zoomFactor, fy=zoomFactor)
    return img, templateDict, frameWidth, frameHeight, frameCenter, imgHeigth, imgWidth


print('COMMANDS\n\'w\',\'a\',\'s\',\'d\' to move around,\n\'z\',\'x\' to zoom in and out\n\'q\'  to exit \npress ENTER to continue')
input()
threshold = 0.95
zoomFactor = 1.01
while True:

    button = cv2.waitKey(1)
    step = 3
    # DOWN
    if button == ord('s') or button == ord('S'):
        frameCenter = (frameCenter[0]+step, frameCenter[1])
    # UP
    if button == ord('w') or button == ord('W'):
        frameCenter = (frameCenter[0]-step, frameCenter[1])
    # LEFT
    if button == ord('a') or button == ord('A'):
        frameCenter = (frameCenter[0], frameCenter[1]-step)
    # RIGHT
    if button == ord('d') or button == ord('D'):
        frameCenter = (frameCenter[0], frameCenter[1]+step)

    #########
    if button == ord('z') or button == ord('Z'):
        img, templateDict, frameWidth, frameHeight, frameCenter, imgHeigth, imgWidth = zoom(
            zoomFactor, img, templateDict, frameWidth, frameHeight, frameCenter)

    if button == ord('x') or button == ord('X'):
        img, templateDict, frameWidth, frameHeight, frameCenter, imgHeigth, imgWidth = zoom(
            1/zoomFactor, img, templateDict, frameWidth, frameHeight, frameCenter)

    #########

    tempImg = img.copy()

    lowerHeightBound = frameCenter[0]-frameHeight//2
    upperHeightBound = frameCenter[0]+frameHeight//2
    lowerWidthBound = frameCenter[1]-frameWidth//2
    upperWidthBound = frameCenter[1]+frameWidth//2

    if lowerHeightBound < 0 or upperHeightBound > imgHeigth or lowerWidthBound < 0 or upperWidthBound > imgWidth:
        print("frame is out of bounds")
        break
    frame = img[lowerHeightBound:upperHeightBound,
                lowerWidthBound:upperWidthBound]

    cv2.rectangle(tempImg, (lowerWidthBound, lowerHeightBound),
                  (upperWidthBound, upperHeightBound), 0, 0)

    for key in templateDict:
        template = templateDict[key]
        templateMask = cv2.bitwise_not(templateDict[key])

        result = cv2.matchTemplate(
            frame, template, cv2.TM_CCORR_NORMED, mask=templateMask)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if(max_val > threshold):
            cv2.rectangle(
                frame, max_loc, (max_loc[0]+template.shape[1], max_loc[1]+template.shape[1]), 255, 10)
            del templateDict[key]
            break


    cv2.imshow('plaketa', tempImg)
    if button == ord('q') or button == ord('Q'):
        break


cv2.destroyAllWindows()
