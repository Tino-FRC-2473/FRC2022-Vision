import cv2
from numpy import array


BLUE_LOWER = array([70, 50, 50])
BLUE_UPPER = array([120, 255, 255])

RED_LOWER = array([120, 50, 50])
RED_UPPER = array([200, 255, 255])


def detect(image, color):
    if color == "blue":
        lower_bound = BLUE_LOWER
        upper_bound = BLUE_UPPER
    elif color == "red":
        lower_bound = RED_LOWER
        upper_bound = RED_UPPER
    else:
        raise Exception('color must be "blue" or "red"')

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    return mask
