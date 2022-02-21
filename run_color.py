from os import listdir
import cv2
from color_detector import detect
import numpy as np

blank = cv2.imread("blank.jpg")
path = "/Users/akshatmehta/Downloads/test_images_revision_2/"


def show_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_and_show(file, color):
    image = cv2.imread(file)
    blurred, yuv, mask = detect(image, color, True)
    output = cv2.bitwise_and(blank, blank, mask=mask)
    show_image(
        f"Detecting {color} in {file[len(path):]}", np.vstack((np.hstack((image, blurred)), np.hstack((yuv, output)))))


def detect_and_save(file, color):
    image = cv2.imread(file)
    result = detect(image, color)
    cv2.imwrite(f"/Users/akshatmehta/Downloads/binary_yuv/{color}_{file[len(path):]}", result)


if __name__ == '__main__':
    for img in listdir(path):
        if "blue" in img or "both" in img:
            detect_and_show(path + img, "blue")
    # for img in listdir(path):
    #     detect_and_show(path + img, "blue")
    # detect_and_show(path + "dark_blue_distance_24_angle_-30_background_elements_N.jpg", "blue")
