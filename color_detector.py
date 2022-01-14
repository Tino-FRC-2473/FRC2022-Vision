class ColorDetector:
    
    def __init__(self, video_name, lower_bound, upper_bound):
        # self.image = cv2.imread(image_name)
        self.video = VideoFileGeneratorFile.VideoFileGenerator(video_name)
        self.lower_bound = np.array(lower_bound)
        self.upper_bound = np.array(upper_bound)
            
    def detect(self):
        
        image = self.video.get_next_frame()

        # Convert BGR to HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        mask = cv2.inRange(hsv, self.lower_bound, self.upper_bound)
        output = cv2.bitwise_and(image,image, mask= mask)
        
        cv2.imshow("Color Detected", np.hstack((image,output)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
