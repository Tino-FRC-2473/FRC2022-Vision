# This file is used to grab images from the camera when the respective keys on the keyboard are
# pressed. This is used to get test images from the webcam and not intended for use in the actual
# competition

import cv2

# use the default camera
input = cv2.VideoCapture(0)

while True:
    try:
        print("ready to capture image")
        # if the 't' key is pressed (t for take photo), then save the image gotten from the camera
        if cv2.waitKey(0) == ord('t'):
            success, image = input.read()
            if not success:
                print("no frames have been grabbed, aborting process")
                break
            cv2.imwrite("distance_#_angle_#.jpg", image)
            cv2.imshow(image, "Saved Image")
        # else if the 's' key is pressed (s for stop), stop waiting for images
        elif cv2.waitKey(0) == ord('s'):
            print("quitting")
            break
    # handle the case when the program is interrupted (control + c)
    except KeyboardInterrupt:
        print("interrupted")
        break

# close the camera
input.release()
print("camera closed")
# destroy all the image windows shows by cv2.imshow() (line 18)
cv2.destroyAllWindows()
