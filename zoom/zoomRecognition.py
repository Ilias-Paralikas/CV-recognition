import cv2
import os
import re


#all the methods that are possible for cv2.matchTemplate function
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
         cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

#recognise templte in image. The temp needs to be the same size and orientation that it will eventually be found 
# in the image
def RecogniseTemplate(img, template, methods=[cv2.TM_CCOEFF]):
    h, w = template.shape
    for method in methods:
        img2 = img.copy()
        result = cv2.matchTemplate(img2,template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc

        cv2.rectangle(img2,location, (location[0]+w, location[1]+h),(255,0,0),10)

        cv2.imshow("method" +str(method),img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



template = cv2.imread('template.jpg',0)

for filename in os.listdir('zoomedImages'):
    img = cv2.imread('zoomedImages/'+filename,0)
    zoom = int(re.sub("[^0-9]","",filename)) /100
    zoomed_template = cv2.resize(template,(0,0),fx= zoom,fy=zoom)
    RecogniseTemplate(img,zoomed_template,methods)
    cv2.waitKey(0)
    cv2.destroyAllWindows()