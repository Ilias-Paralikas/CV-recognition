from typing import OrderedDict
import cv2
import numpy as np
from math import cos, sin


img = np.full((900, 1800), 255, np.uint8)
imgHegith, imgWidth = img.shape
imgCentr = (imgHegith//2, imgWidth//2)

frameHeight = 100
frameWidth = 200
frameCenter = imgCentr

spiralCentrer = imgCentr


def cyclicalToCartesian(range, angle): return (int(range * cos(angle) + spiralCentrer[0]),
                                               int(range * sin(angle)+spiralCentrer[1]))


range = 0
angle = 0
while True:
    range = range+1
    angle = angle + 0.08
    frameCenter = cyclicalToCartesian(range, angle)

    lowerHeightBound = max(0, frameCenter[0]-frameHeight//2)
    upperHeightBound = min(imgHegith, frameCenter[0]+frameHeight//2)
    lowerWidthBound = max(0, frameCenter[1]-frameWidth//2)
    upperWidthBound = min(imgWidth, frameCenter[1]+frameWidth//2)

    frame = img[lowerHeightBound:upperHeightBound,
                lowerWidthBound:upperWidthBound]
    frame &= cv2.bitwise_not(frame)
    cv2.imshow("image", img)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
