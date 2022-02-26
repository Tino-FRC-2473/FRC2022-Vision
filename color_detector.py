import cv2
import numpy as np


RED_LOWER = np.array([0, 50, 140])
RED_UPPER = np.array([200, 150, 255])

BLUE_LOWER = np.array([0, 0, 0])
BLUE_UPPER = np.array([255, 255, 110])


def detect(image, color, return_all=False):

    # HoughCircles code
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 9)
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1, minDist=120, param1=150, param2=30, minRadius=85)
    if circles is not None:
        image_copy = image.copy()
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(image_copy, (x, y), r, (255, 255, 255), -1)
        hsv = cv2.cvtColor(image_copy, cv2.COLOR_BGR2HSV_FULL)
        circle_mask = cv2.inRange(hsv, np.array([0, 0, 255]), np.array([360, 0, 255]))
        image = cv2.bitwise_and(image, image, mask=circle_mask)

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
