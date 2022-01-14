import cv2
import numpy as np

class ColorDetector:
    
    def __init__(self, image_name, lower_bound, upper_bound):
        self.image = cv2.imread(image_name)
        self.lower_bound = np.array(lower_bound)
        self.upper_bound = np.array(upper_bound)
            
    def detect(self):

        # Convert BGR to HSV
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        
        mask = cv2.inRange(hsv, self.lower_bound, self.upper_bound)
        output = cv2.bitwise_and(self.image,self.image, mask= mask)
        
        return output
        
#         cv2.imshow("Color Detected", np.hstack((self.image, output)))
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
