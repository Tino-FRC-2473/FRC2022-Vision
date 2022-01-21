import cv2
import numpy as np


class ColorDetector:

    def __init__(self, image_name, color):
        if color == "blue":
            lower_bound = [70, 50, 50]  # dis48_angle0.png
            upper_bound = [120, 255, 255]
        elif color == "red":
            lower_bound = [0, 25, 25]  # dis26_red_angle0.png
            upper_bound = [20, 255, 255]
        else:
            return
        self.image_name = image_name
        self.image = cv2.imread(self.image_name)
        self.lower_bound = np.array(lower_bound)
        self.upper_bound = np.array(upper_bound)

    def detect(self):

        # Convert BGR to HSV
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, self.lower_bound, self.upper_bound)
        output = cv2.bitwise_and(self.image, self.image, mask=mask)

        # return output

        gray_image = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

        (thresh, blackAndWhiteImage) = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY)

        # cv2.imshow("Color Detected", blackAndWhiteImage)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        cv2.imwrite("binary_" + self.image_name, blackAndWhiteImage)


cd = ColorDetector("images/dis59_both_angle0.png", "blue")
cd.detect()
