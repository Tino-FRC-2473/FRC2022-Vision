from os import listdir
import cv2
from color_detector import ColorDetector
import numpy as np


def show_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def side_by_side_image(title, *images):
    show_image(title, np.concatenate(images))


def detect(path, img, color):
    original = cv2.imread(path + img)
    cd = ColorDetector(original)
    result = cd.detect(color)
    output = cv2.bitwise_and(original, original, mask=result)
    side_by_side_image(f"Detecting {color} in {img}", original, output)


if __name__ == '__main__':
    path = "/Users/akshatmehta/Downloads/test_images_revision_2/"
    for img in listdir(path):
        detect(path, img, "red")
    for img in listdir(path):
        detect(path, img, "blue")
    # detect(path, "light_red_distance_50_angle_30_background_elements_N.jpg", "red")
