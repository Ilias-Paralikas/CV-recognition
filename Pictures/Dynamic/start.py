import enum
from re import template
import cv2
import os
import numpy as np


# we will take this images that represents the whole of the cirsut board
original = cv2.imread('seperatedSymbols.jpg',0)


# make sure that we have the file with the templates that we are looking for
symbolFolder = 'individualTemplates'
if not os.path.isdir(symbolFolder):
    print('File with the symobls does not exist')

#read the symbols from a file all the symbols in a Dict so we can can call  them by their name
symbolDict = {}
for filename in os.listdir(symbolFolder):
    img =  cv2.imread(symbolFolder + '/'+filename, 0)
    name = filename.split('.')[0]
    symbolDict[name] = img

# all the sub images of the original, the values chosen to cut the image are manually picked and have 
# to be adjusted to the picture
subImages = []
for i in range(0,3):
    for j in range(0,4):
        subImages.insert(0,original[i*150:(i+1)*150,j*200:(j+1)*200])



# for every template that is store in the 
for key in symbolDict:
    template = symbolDict[key]
    h, w = template.shape  
    values = []
    for counter, subImage in enumerate(subImages):
        # we will collect the values that mathcTemplate thinks each image matches the template and chose the best one
        result = cv2.matchTemplate(subImage,template,cv2.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        #keep all the values and the possition of the image in the subImages list as well as the location 
        #that we will draw the box
        values.insert(0,(counter,max_loc,max_val))
    
    #sort the list accodring to the values that matched the template
    values.sort(key=lambda x:x[2],reverse=1)
    best_match = values[0]
    
    location = best_match[1]
    cv2.rectangle(subImages[best_match[0]],location, (location[0]+w, location[1]+h),(255,0,0),10)

    cv2.imshow('template',template)
    cv2.imshow('best match' + str(max_val),subImages[best_match[0]])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
