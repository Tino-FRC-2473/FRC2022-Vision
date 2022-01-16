import cv2


class VideoFileGenerator:
    def __init__(self, file_path):
        # set up the video capture device to get frames from the video file
        self.input = cv2.VideoCapture(file_path)
        # capturing variable keeps track of whether or not the video file has reached the end
        self.capturing = True

    def get_next_frame(self):
        # read() combines the use grab() and retreive() methods in cv2 library
        success, image = self.input.read()
        # if there is a valid frame retrieved, then return the image and a True status, otherwise return None and a False status
        if(success):
            return image, True
        else:
            self.capturing = False
            return None, False

    def is_capturing(self):
        return self.capturing
