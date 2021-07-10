import cv2
import os
import sys
sys.path.append("../.")
import shared

original = cv2.imread('symbols.jpg', 0)

dict = {}
symbolFolder = 'individualSymbols'
if not os.path.isdir(symbolFolder):
    print('File with the symobls does not exist')
#save all the symbols in a dict
dict['hashtag'] = cv2.imread(symbolFolder+'/hashtag.jpg', 0)
dict['circle'] = cv2.imread(symbolFolder+'/circle.jpg', 0)
dict['flatC'] = cv2.imread(symbolFolder+'/flatC.jpg', 0)
dict['cross'] = cv2.imread(symbolFolder+'/cross.jpg', 0)
dict['rombos'] = cv2.imread(symbolFolder+'/rombos.jpg', 0)
dict['square'] = cv2.imread(symbolFolder+'/square.jpg', 0)
dict['ex'] = cv2.imread(symbolFolder+'/ex.jpg', 0)


distortedFolder = 'distortedImages'
#match all the symbols
for key in dict:
    template = dict[key]
    #to all the distorted images from the folder
    for filename in os.listdir(distortedFolder):
        img = cv2.imread(distortedFolder + '/'+filename, 0)
        cv2.imshow('template',template)
        shared.RecogniseTemplate(img, template)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

