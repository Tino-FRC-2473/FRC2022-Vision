
from cv2 import cv2
from numpy import array

img_blue = cv2.imread('dark_blue_distance_24_angle_-30_background_elements_N.jpg')
img_red = cv2.imread('dark_red_distance_65_angle_-30_background_elements_N.jpg')

YUV_img = cv2.cvtColor(img_blue, cv2.COLOR_RGB2YUV)

BLUE_LOWER = array([0, 0, 100])
BLUE_UPPER = array([200, 125, 200])

blurred = cv2.blur(YUV_img, (15, 15))

mask = cv2.inRange(blurred, BLUE_LOWER, BLUE_UPPER)


cv2.imshow('YUV img', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
