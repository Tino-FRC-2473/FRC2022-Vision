import serial
import struct
from video_live_generator import VideoLiveGenerator
import color_detector
from ball_detection import BallDetection


auto_camera = VideoLiveGenerator(1)

# open the serial port
ser = serial.Serial('/dev/')
print(ser.name)

# run ball detection indefinitely
while True:
    next_img = auto_camera.get_next_frame()
    # get the binary image
    binary_image = color_detector.detect(next_img, "blue")
    # get the ball distance and angle from the robot
    ball_detector = BallDetection(next_img)
    cv_info = ball_detector.detect_ball()
    print(f"cv_info is: {cv_info}")
    # send the data via the serial port (distance, angle)
    # pack two float types (format 'f', put two of them for 2 arguments)
    # typecast to bytearray for compatability with serial write() method
    print(bytearray(struct.pack("ff", float(cv_info[0]), float(cv_info[1]))))
    ser.write(bytearray(struct.pack("ff", float(cv_info[0]), float(cv_info[1]))))
