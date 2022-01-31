import cv2
import math
import random


class CameraData:
    def __init__(self, camera_tilt):
        self.H_FIELD_OF_VIEW = 68.37
        self.V_FIELD_OF_VIEW = 41.21
        self.CAMERA_TILT = camera_tilt

    def get_horiz_FOV(self):
        return self.H_FIELD_OF_VIEW

    def get_vert_FOV(self):
        return self.V_FIELD_OF_VIEW

    def get_camera_tilt(self):
        return self.CAMERA_TILT
