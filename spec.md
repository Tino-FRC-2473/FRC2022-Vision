# Vision Input
Uses cv2 API

# Responsibilities:
* open/close the camera
* Return the camera video feed as images represented by tuples using the bgr channels
* Field of View
* Handle multiple cameras (processes)

## ImageGenerator
* Returns the image as an tuple (with the bgr values)

### Methods
* get_pixel_channel_values(image, x, y) - returns an tuple with channel values as respectice indices at the specified image pixel
* get_pixel_channel(image, x, y, channel=0) - returns the channel value specified for the image pixel
* get_image_channel(image, channel=0) - returns 2-dimensional tuple with channel values corresponding to the respective indices of the image
* get_image_channel_values(image) - returns 3-dimensional tuple with channel values corresponding to the respective indices of the image

## Video File Generator
* Returns the image that the camera sees (as a 2D or 3D arr)
* Captures video from a video file

### Methods
* get_next_frame(self) - returns the next frame from the video file
* is_capturing(self) - returns the capturing variable

## Video Live Generator
* Returns current image frame 
* Captures video from the camera itself
* Use Multiprocessing to treat each camera as a seperate stream of video input (if more than one camera is used)

### Methods
* get_next_frame(self) - returns the next frame from the video file
* is_capturing(self) - returns the capturing variable (if the camera is currently recording)

## CameraData
* Stores all the camera parameters (takes in a camera in constructor)
* Horizontal and Vertical FOV
* Camera tilt angle
* Screen Size 

### Methods
* get_horiz_FOV(self) - returns camera's horizontal field of view
* get_vert_FOV(self): returns the camera's vertical field of view
* get_camera_tilt(self): Returns the camera's tilt

# Jetson

Involves a collection of shell scripts to run on the Jetson. run2022vision.sh is in the FRC2020-Vision repository and other setup/preparation scripts are in Jetson-Setup.

# Testing
## Test Image Set

Set of videos and pictures from the robot camera perspective for CV testing/training

* Different lighting conditions/shadows
* Different angles and distances from camera to ball
* Both ball colors
* One ball, multiple balls, no balls
* Images with bumpers/other colored field elements

## Test Image Script

Script to get images using OpenCV when a key on the keyboard is clicked. Will be used to collect test images.