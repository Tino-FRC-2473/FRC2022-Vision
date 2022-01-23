import cv2
import numpy
import ball_detection as bd

img = cv2.imread("test_images/dis48_angle10.png")
detect = bd.BallDetection(img)
output = detect.detect_ball()
cv2.imshow('contours image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
