import cv2
import pandas as pd
import ball_detection as bd

img = cv2.imread("test_images/blue_dark_blue_distance_24_angle_30_background_elements_N.jpg")
detect = bd.BallDetection(img)
output = detect.detect_ball()
# resize image for better view
scale_percent = 60  # percent of original size
width = int(output.shape[1] * scale_percent / 100)
height = int(output.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('contours image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ACCURACY TEST

# data = pd.read_csv("test_images.csv")
# test_images = data['file'].tolist()
# dist = data['dist'].tolist()
# pred_dist = []
# percents = []
#
# for test_img in test_images:
#     img = cv2.imread(str(test_img))
#     detect = bd.BallDetection(img)
#     distance = detect.detect_ball()
#     pred_dist.append(distance)
#
# for i in range(len(dist)):
#     if pred_dist[i] != -1 and dist[i] != 0:
#         val = ((pred_dist[i] - dist[i])/dist[i]) * 100
#         percents.append(val)
#     else:
#         continue
#
# acc = 0
# for p in percents:
#     acc = acc + p
# acc = 100-abs(acc/len(dist))
# print("Number of images: ", len(percents))
# print("Percent Accuracy: ", str(acc))
