# from multiprocessing import Process
import time
# import serial
from video_live_generator import VideoLiveGenerator
import color_detector
from ball_detection import BallDetection


driver_camera = VideoLiveGenerator(1)
# track the time to close the camera once the match is over
start_time = time.time()

# open the serial port
# ser = serial.Serial('/dev/')
# print(ser.name)

# run the cv code for 150 seconds (15 for autonomous + 125 for TeleOp)
while (time.time() - start_time) < 150:
    next_img = driver_camera.get_next_frame()
    # get the binary image
    binary_image = color_detector.detect(next_img, "blue")
    # get the ball distance and angle from the robot
    ball_detector = BallDetection(next_img)
    ball_info = ball_detector.detect_ball()
    # get the needed information and start encoding
    cv_info = [float(ball_info[0]), float(ball_info[1]), next_img]
    print(f"cv_info is: {cv_info}")

# close the camera at the end of the time
driver_camera.close_camera()


# auto_camera = VideoLiveGenerator(2)

# driver_station_feed = Process(target=driver_camera.get_next_frame(), name="driver station camera feed")
# autonomous_feed = Process(target=auto_camera.get_next_frame(), name="autonomous camera feed")

# driver_station_feed.start()
# autonomous_feed.start()
