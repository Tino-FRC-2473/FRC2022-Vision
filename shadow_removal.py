
from cv2 import cv2
import numpy as np
from color_detector_hsv import ColorDetectorHSV


img_blue = cv2.imread('/Users/akshatmehta/Downloads/test_images_revision_2/dark_blue_distance_65_angle_-45_background_elements_N.jpg')
img_red = cv2.imread('/Users/akshatmehta/Downloads/test_images_revision_2/light_red_distance_40_angle_-60_background_elements_N.jpg.jpg')

blurred = cv2.blur(img_red, (15, 15))

YUV_img = cv2.cvtColor(blurred, cv2.COLOR_BGR2YUV)

# BLUE_LOWER = np.array([0, 130, 0])
# BLUE_UPPER = np.array([130, 200, 200])

RED_LOWER = np.array([0, 50, 150])
RED_UPPER = np.array([200, 150, 255])

mask = cv2.inRange(YUV_img, RED_LOWER, RED_UPPER)

blank = np.full((1080, 1920, 3), 255, dtype=np.uint8)
mask = cv2.bitwise_and(blank, blank, mask=mask)
hsv = ColorDetectorHSV(img_red).detect("red")
hsv = cv2.bitwise_and(blank, blank, mask=hsv)
cv2.imshow('YUV img', np.hstack((np.vstack((img_red, YUV_img)), np.vstack((hsv, mask)))))
cv2.waitKey(0)
cv2.destroyAllWindows()
