import cv2
from numpy import array


class ColorDetector:

    BLUE_LOWER = array([70, 50, 50])
    BLUE_UPPER = array([120, 255, 255])

    RED_LOWER = array([120, 50, 50])
    RED_UPPER = array([200, 255, 255])

    def __init__(self, image):
        self.image = image

    def detect(self, color):

        if color == "blue":
            lower_bound = self.BLUE_LOWER
            upper_bound = self.BLUE_UPPER
        elif color == "red":
            lower_bound = self.RED_LOWER
            upper_bound = self.RED_UPPER
        else:
            raise Exception('color must be "blue" or "red"')

        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        return mask
