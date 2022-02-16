import serial
import ball_detection as bd


class Encoding:
    def __init__(self):
        '''
        code to test:
        def __init__(self, name = "ttyS0"):
        self.s = serial.Serial("/dev/")
        print(s.name)
        s.write('Hello World!')
        s.close()
        '''
        '''
        img = cv2.imread("test_images/blue_dark_blue_distance_24_angle_30_background_elements_N.jpg")
        ball = bd.BallDetection(img)
        '''


    def send_data(self, ball_data, s): # ball_data: array from cv, s: serial port opened by cv
        data_string = "".join("\n{d}\n{d}\n".format(round(ball_data[0], 2), round(ball_data[1], 2))) # ball_data[0] = distance, #ball_data[1] = angle
        # one line break: new value (angle), two line breaks: end of data
        print("X " + data_string + " E")
        s.write(bytes("X" + data_string + " E", "utf-8")) # "X" = start, "E" = end