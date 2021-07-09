import cv2
from sharedResources import methods
from sharedResources import RecogniseTemplate

img = cv2.imread('image.jpg',0)
template = cv2.imread('template.jpg',0)

RecogniseTemplate(img,template,methods)


