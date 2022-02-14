import cv2
from multiprocessing import Process
from video_live_generator import VideoLiveGenerator

driver_camera = VideoLiveGenerator(1)
auto_camera = VideoLiveGenerator(2)

driver_station_feed = Process(target=driver_camera.get_next_frame(), name="driver station camera feed")
autonomous_feed = Process(target=auto_camera.get_next_frame(), name="autonomous camera feed")

driver_station_feed.start()
autonomous_feed.start()
