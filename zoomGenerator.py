import cv2
import os
from sharedResources import zoomFactors
from sharedResources import initializeFolder


original = cv2.imread('image.jpg',0)

initializeFolder('zoomedImages')

for zoom in zoomFactors:
    name = "zoomedImages/zoom" + str(int(zoom*100)) + '.jpg'
    tempImg = cv2.resize(original,(0,0),fx=zoom,fy=zoom)
    cv2.imwrite(name,tempImg)