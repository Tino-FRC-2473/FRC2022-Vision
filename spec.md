# Vision Input
Uses cv2 API

# Responsibilities:
* open/close the camera
* Return the camera video feed as images represented by ndarrays using the bgr channels
* Field of View
* Handle multiple cameras (processes)

## ImageGenerator
* Returns the image as an ndarray (with the bgr values)

## Video File Generator
* Returns the image that the camera sees (as a 2D or 3D arr)
* Captures video from a video file
* Use Multiprocessing to treat each camera as a seperate stream of video input (if more than one camera is used)

## Video Live Generator
* Returns current image frame 
* Captures video from the camera itself

## CameraData
* Stores all the camera parameters (takes in a camera in constructor)
* Horizontal and Vertical FOV
* Camera tilt angle
* Screen Size 

### Methods
* getImageArr(): Returns rgb/yuv image ndarray
* getHorizFOV(): getVertFOV():Returns horizontal and vertical field of view
* getImage(): Returns the raw image from the camera feed

# Jetson

Involves a collection of shell scripts to run on the Jetson. run2022vision.sh is in the FRC2020-Vision repository and other setup/preparation scripts are in Jetson-Setup.

# Driver/testing file
* Runs the main program
* Tests if the camera methods work

# Test Image Set

Set of videos and pictures from the robot camera perspective for CV testing/training

* Different lighting conditions/shadows
* Different angles and distances from camera to ball
* Both ball colors
* One ball, multiple balls, no balls
* Images with bumpers/other colored field elements
