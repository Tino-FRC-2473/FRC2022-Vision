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

        # return mask

        self.show_image(mask)

        # cv2.imwrite("binary_" + self.image_name, mask)

    def show_image(self, image):
        cv2.imshow("Color Detected", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    cd = ColorDetector("images/dis48_angle0.png", "blue")
    cd.detect()
