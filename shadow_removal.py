import cv2
import numpy as np

img = cv2.imread('dark_blue_distance_24_angle_-30_background_elements_N.jpg')

rows, cols = img.shape[:2]

kernel = np.ones((25, 25), np.float32) / 625.0
output_kernel = cv2.filter2D(img, -1, kernel)

output_blur = cv2.blur(img, (25, 25))
output_box = cv2.boxFilter(img, -1, (5, 5), normalize=False)
output_gaus = cv2.GaussianBlur(img, (5, 5), 0)
output_med = cv2.medianBlur(img, 5)
output_bil = cv2.bilateralFilter(img, 5, 6, 6)

cv2.imshow('Original', img)
# cv2.imshow('kernel blur', output_kernel)
cv2.imshow('Blur() output', output_blur)
# cv2.imshow('Box filter', output_box)
# cv2.imshow('Gaussian', output_gaus)
# cv2.imshow('Bilateral', output_bil)
# cv2.imshow('Median Blur', output_med)

cv2.waitKey(0)