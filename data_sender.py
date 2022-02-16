# from multiprocessing import Process
from video_live_generator import VideoLiveGenerator
from color_detector import ColorDetector
from ball_detection import BallDetection


driver_camera = VideoLiveGenerator(1)

while True:
    next_img = driver_camera.get_next_frame()
    # create a new instance of the ColorDetector class and BallDetection class to get ball information
    color_detection = ColorDetector(next_img)
    binary_image = color_detection.detect()
    ball_detector = BallDetection(binary_image)
    ball_info = ball_detector.detect_ball()

# auto_camera = VideoLiveGenerator(2)

# driver_station_feed = Process(target=driver_camera.get_next_frame(), name="driver station camera feed")
# autonomous_feed = Process(target=auto_camera.get_next_frame(), name="autonomous camera feed")

# driver_station_feed.start()
# autonomous_feed.start()
