import cv2
from numpy import array


RED_LOWER = array([0, 50, 140])
RED_UPPER = array([200, 150, 255])

BLUE_LOWER = array([0, 0, 0])
BLUE_UPPER = array([255, 255, 110])


def detect(image, color, return_all=False):

    blurred = cv2.blur(image, (15, 15))
    yuv = cv2.cvtColor(blurred, cv2.COLOR_BGR2YUV)

    if color == "blue":
        mask = cv2.inRange(yuv, BLUE_LOWER, BLUE_UPPER)
    elif color == "red":
        mask = cv2.inRange(yuv, RED_LOWER, RED_UPPER)
    else:
        raise Exception('color must be "blue" or "red"')

    if return_all:
        return blurred, yuv, mask
    else:
        return mask
