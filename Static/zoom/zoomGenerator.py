import cv2
import os
import sys
sys.path.append("../../.")
import shared


foldefname = 'zoomedImages'
shared.initializeFile(foldefname)

#this is needed to create different test cases and to zoom the teplate
zoomFactors = [0.20,0.40,0.60,0.80,1.20,1.40,1.60,1.80,2.00]


original = cv2.imread('image.jpg',0)

#create and store images zoomed in and out
for zoom in zoomFactors:
    #save the zoom of the picture in the filename
    filename = foldefname + "/zoom" + str(int(zoom*100)) + '.jpg'
    tempImg = cv2.resize(original,(0,0),fx=zoom,fy=zoom)
    cv2.imwrite(filename,tempImg)