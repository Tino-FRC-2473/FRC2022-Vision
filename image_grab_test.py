# This file is used to grab images from the camera when the respective keys on the keyboard are
# pressed. This is used to get test images from the webcam and not intended for use in the actual
# competition

import cv2

# use the default camera
input = cv2.VideoCapture(0)

print("ready to capture image")
#create a window first to allow cv2.waitKey(0) to work
success, image = input.read()
cv2.imshow("Saved Image", image)

while True:
    try:
        # if the 't' key is pressed (t for take photo), then save the image gotten from the camera
        if cv2.waitKey(0) == ord('t'):
            success, image = input.read()
            if not success:
                print("\nno frames have been grabbed, aborting process")
                break
            cv2.imwrite("distance_#_angle_#.jpg", image)
            cv2.imshow("Saved Image", image)
        # else if the 's' key is pressed (s for stop), stop waiting for images
        elif cv2.waitKey(0) == ord('s'):
            print("\nquitting")
            break
        else:
            print("nothing is happening")
    # handle the case when the program is interrupted (control + c)
    except KeyboardInterrupt:
        print("\ninterrupted")
        break

# close the camera
input.release()
print("camera closed")
# destroy all the image windows shows by cv2.imshow() (line 18)
cv2.destroyAllWindows()
