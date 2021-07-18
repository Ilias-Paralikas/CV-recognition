import cv2
import os
import sys
sys.path.append("../../.")
import shared

original = cv2.imread('symbols.jpg', 0)

symbolFolder = 'individualSymbols'
if not os.path.isdir(symbolFolder):
    print('File with the symobls does not exist')
#save all the symbols in a dict

dict = {}

for filename in os.listdir(symbolFolder):
    img =  cv2.imread(symbolFolder + '/'+filename, 0)
    name = filename.split('.')[0]
    dict[name] = img


distortedFolder = 'distortedImages'
#match all the symbols
for key in dict:
    template = dict[key]
    #to all the distorted images from the folder
    for filename in os.listdir(distortedFolder):
        img = cv2.imread(distortedFolder + '/'+filename, 0)
        # find the symbol in the given image
        shared.RecogniseTemplate(img, template)
