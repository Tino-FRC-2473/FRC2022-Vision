# this file will be used to get images from the live camera feed

import cv2


class VideoLiveGenerator():
    def __init__(self, camera_port=0):
        self.camera_port = camera_port
        # stores the camera input video stream object
        self.live_input = cv2.VideoCapture(self.camera_port)
        # keeps track if the camera is still recording video
        self.capturing = False

    def get_next_frame(self):
        # read() combines the get() and retrive() methods, gets the next image from the camera video feed
        self.capturing, image = self.live_input.read()
        return image

    def is_capturing(self):
        return self.capturing
