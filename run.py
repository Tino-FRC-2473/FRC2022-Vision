from os import listdir
import cv2
from color_detector_yuv import ColorDetector
import numpy as np

blank = cv2.imread("blank.jpg")


def show_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_and_show(file, color):
    image = cv2.imread(file)
    cd = ColorDetector(image)
    blurred, hsv, mask = cd.detect(color, True)
    output = cv2.bitwise_and(blank, blank, mask=mask)
    show_image(f"Detecting {color} in {file[52:]}", np.vstack((np.hstack((image, blurred)), np.hstack((hsv, output)))))


def detect_and_save(file, color):
    original = cv2.imread(file)
    cd = ColorDetector(original)
    result = cd.detect(color)
    cv2.imwrite(f"/Users/akshatmehta/Downloads/binary_yuv/{color}_{file[52:]}", result)


if __name__ == '__main__':
    path = "/Users/akshatmehta/Downloads/test_images_revision_2/"
    for img in listdir(path):
        if "blue" in img or "both" in img:
            detect_and_show(path + img, "blue")
    # for img in listdir(path):
    #     detect_and_show(path + img, "blue")
    # detect_and_show(path + "dark_blue_distance_24_angle_-30_background_elements_N.jpg", "blue")