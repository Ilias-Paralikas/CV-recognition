# a lot of scripts use the same variables, functions etc, and in case of variables they need to be the same
#so they are stored here so we dont have to change them in all of the files 
import cv2
import os

# make a file if it does not exist , or empty it if it does
def initializeFolder(name):
    if not os.path.isdir(name ):
        os.system('mkdir'+name)
    else :
        os.system('rm -rf /home/ilias/Documents/GitHub/CV-recognition/'+name +'/*')
#this is needed to create different test cases and to zoom the teplate
zoomFactors = [0.20,0.40,0.60,0.80,1.20,1.40,1.60,1.80,2.00]

#all the methods, we will eventually chose one
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

