import cv2
import os


# make a file if it does not exist , or empty it if it does from previous calls
if not os.path.isdir('zoomedImages' ):
    os.system('mkdir zoomedImages')
else :
    os.system('rm -rf /home/ilias/Documents/GitHub/CV-recognition/zoomedImages/*')

#this is needed to create different test cases and to zoom the teplate
zoomFactors = [0.20,0.40,0.60,0.80,1.20,1.40,1.60,1.80,2.00]


original = cv2.imread('image.jpg',0)

#create and store images zoomed in and out
for zoom in zoomFactors:
    name = "zoomedImages/zoom" + str(int(zoom*100)) + '.jpg'
    tempImg = cv2.resize(original,(0,0),fx=zoom,fy=zoom)
    cv2.imwrite(name,tempImg)