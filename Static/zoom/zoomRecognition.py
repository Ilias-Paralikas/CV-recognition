import cv2
import os
import re
import sys
sys.path.append("../../.")
import shared


template = cv2.imread('template.jpg', 0)

foldername = 'zoomedImages'
for filename in os.listdir(foldername):
    img = cv2.imread(foldername + '/'+filename, 0)
    # get the zoom of the images from the filename
    zoom = int(re.sub("[^0-9]", "", filename)) / 100
    # zoom the template accordingly
    zoomed_template = cv2.resize(template, (0, 0), fx=zoom, fy=zoom)
    shared.RecogniseTemplate(img, zoomed_template)
