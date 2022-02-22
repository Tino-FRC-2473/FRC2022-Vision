import cv2
import numpy as np

# Camera Constants
KNOWN_DIAMETER_IN = 9.5  # in
# ADJ_FOCAL_LENGTH = 1480.1
FOCAL_LENGTH = 1367.043233  # 83.3% accuracy. Use 1645.101 -> 99.73% accuracy but overshoots
RADIUS_THRESH = 85
MIN_BORDERS = 6
CAMERA_TILT_DOWNWARDS = 20


# CV Input Code
def draw_image_annotations(image, angle, distance):
    cv2.putText(image, f"Angle: {angle} deg.", (875, 100), 0, 1.0, (255, 0, 255), 3)
    cv2.putText(image, f"Distance: {distance} in.", (875, 200), 0, 1.0, (255, 0, 255), 3)


# CV Color Detection Code
RED_LOWER = np.array([0, 50, 140])
RED_UPPER = np.array([200, 150, 255])

BLUE_LOWER = np.array([0, 0, 0])
BLUE_UPPER = np.array([255, 255, 110])


def detect(image, color):

    blurred = cv2.blur(image, (15, 15))
    yuv = cv2.cvtColor(blurred, cv2.COLOR_BGR2YUV)

    if color == "blue":
        mask = cv2.inRange(yuv, BLUE_LOWER, BLUE_UPPER)
    elif color == "red":
        mask = cv2.inRange(yuv, RED_LOWER, RED_UPPER)
    else:
        raise Exception('color must be "blue" or "red"')

    blank = np.full((len(mask), len(mask[0]), 3), 255)
    mask = cv2.bitwise_and(blank, blank, mask=mask)

    return mask


# CV Ball Detection Code
# from imutils github page
def grab_contours(cnts):
    # if the length the contours tuple returned by cv2.findContours
    # is '2' then we are using either OpenCV v2.4, v4-beta, or
    # v4-official
    if len(cnts) == 2:
        cnts = cnts[0]

    # if the length of the contours tuple is '3' then we are using
    # either OpenCV v3, v4-pre, or v4-alpha
    elif len(cnts) == 3:
        cnts = cnts[1]

    # otherwise OpenCV has changed their cv2.findContours return
    # signature yet again and I have no idea WTH is going on
    else:
        raise Exception(("Contours tuple must have length 2 or 3, otherwise OpenCV changed their cv2.findContours return signature yet again. Refer to OpenCV's documentation in that case"))

    # return the actual contours array
    return cnts


class BallDetection:

    def __init__(self, frame):
        self.frame = frame
        self.x_val = int(frame.shape[1])
        self.y_val = int(frame.shape[0])

    def detect_ball(self):
        distance = -1
        angle = -1
        frame_1 = cv2.cvtColor(self.frame, cv2.COLOR_YUV2RGB)
        frame = cv2.cvtColor(frame_1, cv2.COLOR_RGB2GRAY)
        self.prep_frame()
        cnts = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cnts = grab_contours(cnts)

        if len(cnts) > 0:
            for cnt in cnts:
                ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                if radius >= RADIUS_THRESH:
                    # determine the num of border points on the contour (ex: differentiates between circle and rect)
                    perimeter = cv2.arcLength(cnt, closed=True)
                    borders = cv2.approxPolyDP(curve=cnt, epsilon=0.0085 * perimeter, closed=True)
                    if len(borders) > MIN_BORDERS:
                        angle = self.find_angle(x, y)
                        # print(radius)
                        distance = self.find_distance(radius)
                    cv2.circle(self.frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
        return distance, angle

    def transform(self, x, y):
        # transform coordinates to a system with the origin at the bottom-middle of screen
        dims = self.frame.shape
        x = x - (dims[1] / 2)
        y = dims[0] - y
        return x, y

    def find_angle(self, x, y):
        tsfm_x, tsfm_y = self.transform(x, y)
        angle_rad = np.arctan(abs(tsfm_x) / tsfm_y)
        angle_deg = round(np.degrees(angle_rad), 2)

        # angle annotations
        cv2.putText(self.frame, "Angle: " + str(angle_deg) + " degrees", (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (200, 200, 0), 1)
        cv2.line(self.frame, (int(self.x_val / 2), self.y_val), (int(x), int(y)), (0, 0, 255), 2)
        return angle_deg

    def find_distance(self, radius):
        dist = (KNOWN_DIAMETER_IN * FOCAL_LENGTH) / (radius * 2)
        # print("Distance: " + str(dist))
        return dist

    def prep_frame(self):
        # draw axes on screen for visualization
        cv2.line(self.frame, (int(self.x_val / 2), self.y_val), (int(self.x_val / 2), 0), (0, 0, 255), 2)
        cv2.line(self.frame, (0, self.y_val), (self.x_val, self.y_val), (0, 0, 255), 3)


# runPipeline() is called every frame by Limelight's backend.
def runPipeline(image, llrobot):
    binary_image = detect(image, "blue")

    ball_detect = BallDetection(binary_image)
    distance, angle = ball_detect.detect_ball()

    draw_image_annotations(image, angle, distance)

    # record the distance and angle of the ball to the robot to send back to the robot
    llpython = [float(distance), float(angle)]

    print(f"distance: {distance}, angle: {angle}")

    # return the largest countour, modified image, and custom robot data
    return [], image, llpython
