import cv2
import os
import random

def readTemplates(templateFolder='individualTemplates'):
    # make sure that we have the file with the templates that we are looking for
    if not os.path.isdir(templateFolder):
        print('File with the symobls does not exist')

    #read the templates from a file all the templates in a Dict so we can can call  them by their name
    templateDict = {}
    for filename in os.listdir(templateFolder):
        template =  cv2.imread(templateFolder + '/'+filename, 0)
        name = filename.split('.')[0]
        templateDict[name] = template
    return templateDict


def findBestTemplateMatch(templateDict):
    currentMax =0
    for key in templateDict:
        template = templateDict[key]
        template_mask = cv2.bitwise_not(template)

        result = cv2.matchTemplate(img,template, cv2.TM_CCORR_NORMED,mask=template_mask)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > currentMax:
            tempName = key
            location = max_loc  
            dimentions = template.shape
            currentMax = max_val
    return tempName, location, dimentions, currentMax


img = cv2.imread('image.jpg',0)


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i][j] = img[i][j]+random.randint(0,50)


opening = cv2.morphologyEx(img, cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)))


templateDict = readTemplates()
tempName, location, dimentions, max_val = findBestTemplateMatch(templateDict)

h, w = dimentions
cv2.rectangle(img,location, (location[0]+w, location[1]+h),(255,0,0),10)
cv2.imshow('template', templateDict[tempName])
cv2.imshow('mask', cv2.bitwise_not(templateDict[tempName]))
cv2.imshow(str(max_val),img)
cv2.waitKey(0)
cv2.destroyAllWindows()