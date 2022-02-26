import cv2
import pandas as pd
import ball_detection as bd

img = cv2.imread("test_images/red_dark_red_distance_24_angle_30_background_elements_N.jpg")
detect = bd.BallDetection(img)
data = detect.detect_ball()  # format: [dist, angle] dist & angle are floats
print(data)

if data[0] and data[1]:
    data = f"[{data[0]}, {data[1]}"
    # encode the "data" variable and send over serial