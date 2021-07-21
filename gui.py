################################################################################################################
# This is a working model for the project
# When applied to real world laser ptining, changes will need to be made
# More specifically:
#       img         ->  The whole of the board that is to be printed on and will NOT BE KNOWN!
#                       Thus there will not be such a variable in the finished project
#       
#       frame       ->  The frame will be what the camera detects at any point in time, so we will not have to
#                       define it's size and location
#       
#       zoomFactor  ->  zoomFactor is a result of the elecation of the board at any time, so we wont need to 
#                       to define it, BUT we will need to calculate it !!
#       
#       zoom (Func) ->  This function will need to ONLY zoom in/out the templates, we img will not be present 
#                       and frame will be the input from the camera, which we wont need to modify
#
#       threshold   ->  This variable defines how much a current much resemble a template, to be considered a match
#                       it will need to be defined experimentally
#
#       button      ->  Will be removed as we dont control the camera from user input 
#       (controls)
#
#       
#     
# As a lot of changes will need to ba made, they will be  indicated in the code with 
# REMOVED{ '''code'''  REMOVED} for the ones that will not be needed
# CHANGED{ '''code'''  CHANGED} 
################################################################################################################

import cv2
from math import cos, sin
import os


# REMOVED {
# Read the image 
imgFile = 'rescourses/plaketa.jpg'
img = cv2.imread(imgFile, 0)
imgHeigth, imgWidth = img.shape

# define the frame size and starting possiton
frameHeight = 200
frameWidth = 200
frameCenter = (imgHeigth//2, imgWidth//2)
# REMOVED }


# read the templates from a file all the templates in a Dict so we can can call  them by their name
templateFolder = 'rescourses/templates'
templateDict = {}
# get every file from  templateFolder
for filename in os.listdir(templateFolder):
    # get the image
    template = cv2.imread(templateFolder + '/'+filename, 0)
    # as well as it's name
    name = filename.split('.')[0]
    # store it in the dict
    templateDict[name] = template
    # we will remove this as we dont defince frameHeight and Width manually
    
    # REMOVED {
    if(template.shape[0] > frameHeight or template.shape[1] > frameWidth):
        print('Template needs to fit in the frame, but has bigger dimentions')
        quit()
    # REMOVED }

# the zoom (Func)
def zoom(zoomFactor, img, templateDict, frameWidth, frameHeight, frameCenter):

    # REMOVED { as we wont need to create the img and frame
    img = cv2.resize(img, (0, 0), fx=zoomFactor, fy=zoomFactor)
    imgHeigth, imgWidth = img.shape

    frameWidth = int(frameWidth * zoomFactor)
    frameHeight = int(frameHeight * zoomFactor)
    frameCenter = (int(frameCenter[0] * zoomFactor),
                   int(frameCenter[1] * zoomFactor))
    # REMOVED }

    for key in templateDict:
        templateDict[key] = cv2.resize(
            templateDict[key], (0, 0), fx=zoomFactor, fy=zoomFactor)

    # CHANGED { to '''return templateDict''' as it is the only this modified
    return img, templateDict, frameWidth, frameHeight, frameCenter, imgHeigth, imgWidth
    # CHANGED }


# REMOVED {
print('COMMANDS\n\'w\',\'a\',\'s\',\'d\' to move around,\n\'z\',\'x\' to zoom in and out\n\'q\'  to exit \npress ENTER to continue')
input()
zoomFactor = 1.01
# REMOVED }

# changed???
threshold = 0.95


while True:
    # REMOVED {
    # we wont control the camera from the terminal so we dont need the controls
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

    # zoom in
    if button == ord('z') or button == ord('Z'):
        img, templateDict, frameWidth, frameHeight, frameCenter, imgHeigth, imgWidth = zoom(
            zoomFactor, img, templateDict, frameWidth, frameHeight, frameCenter)
    # zoom out
    if button == ord('x') or button == ord('X'):
        img, templateDict, frameWidth, frameHeight, frameCenter, imgHeigth, imgWidth = zoom(
            1/zoomFactor, img, templateDict, frameWidth, frameHeight, frameCenter)
    # exit
    if button == ord('q') or button == ord('Q'):
        break
    

    # we wont need to define the frame and draw on tempImg in order to display it 
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


    # REMOVED }


    for key in templateDict:
        template = templateDict[key]
        # CHANGED ?? we need to see how well it works with and without the mask
        templateMask = cv2.bitwise_not(templateDict[key])

        result = cv2.matchTemplate(
            frame, template, cv2.TM_CCORR_NORMED, mask=templateMask)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        print(max_val)
        if(max_val > threshold):
            # CHANGED { we wont need to draw a rectangle around the template
            # what we will need to do is, from a known hash table we will need to match the key value
            # to it's location on the board and this find the point (0,0)
            cv2.rectangle(
                frame, max_loc, (max_loc[0]+template.shape[1], max_loc[1]+template.shape[1]), 255, 10)
            # CHANGED }
            del templateDict[key]
            break

    # REMOVED { we wont need to visualise it
    cv2.imshow('plaketa', tempImg)



cv2.destroyAllWindows()
# REMOVED }