#WARNING this is a slow script so run it as few times as possible
import cv2
import random
import sys
sys.path.append("../../.")
import shared

original = cv2.imread('symbols.jpg', 0)
imageHeight, imageWidth = original.shape

foldefname = 'distortedImages'
shared.initializeFile(foldefname)


# chosen at random, will be adjusted later
distorsionLevels = [0.7,0.8,0.9] 
# we distort the images to see how much the algortithm can take
for distorsionLevel in distorsionLevels:
    img = original.copy()
    filename = foldefname + '/dist' + str(int(distorsionLevel*100)) + '.jpg'
    for w in range(imageWidth):
        for h in range(imageHeight):
            if img[h][w] == 0:
                img[h][w] = int(random.randint(0, 255) * distorsionLevel)
            else :
                img[h][w] = 255 - int(random.randint(0, 255) * distorsionLevel)
    cv2.imwrite(filename,img)   