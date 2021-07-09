import cv2
import os
import re
from sharedResources import RecogniseTemplate
from sharedResources import methods

template = cv2.imread('template.jpg',0)

for filename in os.listdir('zoomedImages'):
    img = cv2.imread('zoomedImages/'+filename,0)
    zoom = int(re.sub("[^0-9]","",filename)) /100
    zoomed_template = cv2.resize(template,(0,0),fx= zoom,fy=zoom)
    RecogniseTemplate(img,zoomed_template,methods)
    cv2.waitKey(0)
    cv2.destroyAllWindows()