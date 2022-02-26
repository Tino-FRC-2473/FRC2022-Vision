import cv2
import numpy as np
import imutils
import math

KNOWN_DIAMETER_IN = 9.5  # in
FOCAL_LENGTH = 1367.043233  # 94% accuracy
RADIUS_THRESH = 85
MIN_BORDERS = 5
FOV = 78
DIM = 1920


class BallDetection:

    def __init__(self, frame):
        self.frame = frame
        self.x_val = int(frame.shape[1])
        self.y_val = int(frame.shape[0])

    def detect_ball(self):
        distance = -1
        area = -1
        angle = -1
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        self.prep_frame()
        cnts = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cnts = imutils.grab_contours(cnts)

        if len(cnts) > 0:
            for cnt in cnts:
                ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                if radius >= RADIUS_THRESH:
                    perimeter = cv2.arcLength(cnt, closed=True)
                    borders = cv2.approxPolyDP(curve=cnt, epsilon=0.0085 * perimeter, closed=True)
                    if len(borders) >= MIN_BORDERS:
                        if cv2.contourArea(cnt) > area:  # finding the closest ball
                            area = cv2.contourArea(cnt)
                            distance = self.find_distance(area)
                            angle = self.find_angle(x, y)
                        cv2.circle(self.frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
        return [distance, angle]

    def find_angle(self, x, y):
        center = DIM/2
        diff = center - x
        angle = math.degrees(math.atan(diff/FOCAL_LENGTH))
        # angle annotations
        cv2.putText(self.frame, "Angle: " + str(angle) + " degrees", (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (200, 200, 0), 1)
        return angle

    def find_distance(self, area):
        # DIST USING CONTOUR AREA
        # square root
        dist = 34437*(area**-0.593)
        return dist

    def prep_frame(self):
        # draw axes on screen for visualization
        cv2.line(self.frame, (int(self.x_val / 2), self.y_val), (int(self.x_val / 2), 0), (0, 0, 255), 2)
        cv2.line(self.frame, (0, self.y_val), (self.x_val, self.y_val), (0, 0, 255), 3)
