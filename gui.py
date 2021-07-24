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
# REMOVED { '''code'''  REMOVED } 
# CHANGED { '''code'''  CHANGED }
################################################################################################################

import cv2
from math import cos, sin
import os
import pickle

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
templateImageDict = {}
# get every file from  templateFolder
for filename in os.listdir(templateFolder):
    # get the image
    template = cv2.imread(templateFolder + '/'+filename, 0)
    # as well as it's name (ignore the .jpg part)
    name = filename.split('.')[0]
    # store it in the dict
    templateImageDict[name] = template
   
    # REMOVED {  we will remove this as we dont define frameHeight and Width inside the program
    if(template.shape[0] > frameHeight or template.shape[1] > frameWidth):
        print('Template needs to fit in the frame, but has bigger dimentions')
        quit()
    # REMOVED }


# the zoom (Func)

def zoom(zoomFactor, img, templateImageDict, frameWidth, frameHeight, frameCenter):

    # REMOVED { as we wont need to resize the img and frame 
    img = cv2.resize(img, (0, 0), fx=zoomFactor, fy=zoomFactor)
    imgHeigth, imgWidth = img.shape

    frameWidth = int(frameWidth * zoomFactor)
    frameHeight = int(frameHeight * zoomFactor)
    frameCenter = (int(frameCenter[0] * zoomFactor),
                   int(frameCenter[1] * zoomFactor))
    # REMOVED }

    for key in templateImageDict:
        templateImageDict[key] = cv2.resize(
            templateImageDict[key], (0, 0), fx=zoomFactor, fy=zoomFactor)

    # CHANGED { to '''return templateImageDict''' as it is the only this modified
    return img, templateImageDict, frameWidth, frameHeight, frameCenter, imgHeigth, imgWidth
    # CHANGED }


# get the locations of each template
# They must be manually loaded useing templateLocations.py before the program is run
templateLocationDictFile = 'rescourses/locationDict'
with open(templateLocationDictFile + '.pkl', 'rb') as file:
    templateLocationDict = pickle.load(file)

# see if the keys of the location and template dict match, if they dont there might have been a mistake by the user
for templateKey in templateImageDict:
    if not templateKey in templateLocationDict:
        print('ERROR! template ', templateKey,
              '  is present as a template image, but it\'s location is not in locationDict (run templateLocations.py to register it)')
        quit()

# REMOVED {
print('COMMANDS\n\'w\',\'a\',\'s\',\'d\' to move around,\n\'z\',\'x\' to zoom in and out\n\'q\'  to exit \npress ENTER to continue')
input()
# REMOVED }

# CHANGED { we only need the zoomFactor, based on the elevation of the camera, to resize the templates accordingly
zoomFactor = 1.01
# CHANGED }


# CHANGED { some trial and error should do it
threshold = 0.95
# CHANGED }

while True:
    # REMOVED { we wont control the camera from this script so we dont need the controls
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

    # exit
    if button == ord('q') or button == ord('Q'):
        break
    # REMOVED }



    # CHANGED {  we wont need to zoom and out, if we move the Z axis of the board
    # Also we will need to call this function at the beggining, based on the current elevation, to adjust the
    # initial size of the templates
    # zoom in
    if button == ord('z') or button == ord('Z'):
        img, templateImageDict, frameWidth, frameHeight, frameCenter, imgHeigth, imgWidth = zoom(
            zoomFactor, img, templateImageDict, frameWidth, frameHeight, frameCenter)
    # zoom out
    if button == ord('x') or button == ord('X'):
        img, templateImageDict, frameWidth, frameHeight, frameCenter, imgHeigth, imgWidth = zoom(
            1/zoomFactor, img, templateImageDict, frameWidth, frameHeight, frameCenter)

    # CHANGED }

    # REMOVED { we will not need to generate the the frame as a subimage of img, as it will be provided to us by
    # the camera
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


    # for every frame, see if any templates match is greater than the threshold
    for key in templateImageDict:
        template = templateImageDict[key]

        # match the template
        # ALL the possible methods are
        # methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
        #    'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
        # we chose TM_CCORR_NORMED, but others can be tried

        # WARNING! if [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED] are used, use min_loc, the third variable, which is
        # currently blank instead of max_loc
        result = cv2.matchTemplate(
            frame, template, method=cv2.TM_CCORR_NORMED)
        # the two variables that are blank are min_val and min_loc
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if(max_val > threshold):
            # CHANGED { we wont need to draw a rectangle around the template
            # what we will need to do is, from a known hash table we will need to match the key value
            # to it's location on the board and this find the point (0,0)
            cv2.rectangle(
                frame, max_loc, (max_loc[0]+template.shape[1], max_loc[1]+template.shape[1]), 255, 10)
            # CHANGED }
            print(key, "found at :", templateLocationDict[key])
            del templateImageDict[key]
            break

    # REMOVED { we wont need to visualise it
    cv2.imshow('plaketa', tempImg)


cv2.destroyAllWindows()
# REMOVED }
