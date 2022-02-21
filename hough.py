import numpy as np
import cv2

RED_LOWER = np.array([0, 50, 140])
RED_UPPER = np.array([200, 150, 255])

image = cv2.imread(
    "/Users/akshatmehta/Downloads/test_images_revision_2/light_both_distance_65_angle_30_background_elements_Y.jpg")
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 20, minRadius=500)
