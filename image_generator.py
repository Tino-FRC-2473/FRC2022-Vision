import cv2


# returns an tuple with channel values as respectice indices at the specified image pixel
def get_pixel_channel_values(image, x, y):
    return image[x, y][0], image[x, y][1], image[x, y][2]


# returns the channel value specified for the image pixel
def get_pixel_channel(image, x, y, channel=0):
    return image[x, y, channel]


# returns 2-dimensional tuple with channel values corresponding to the respective indices of the image
def get_image_channel(image, channel=0):
    image_list = list()
    for x in range(len(image)):
        image_channel_values = list()
        for y in range(len(image[0])):
            image_channel_values.append(get_pixel_channel(image, x, y, channel))
        image_list.append(image_channel_values)
    return tuple(image_list)


# returns 3-dimensional tuple with channel values corresponding to the respective indices of the image
def get_image_channel_values(image):
    image_list = list()
    for x in range(len(image)):
        image_channel_values = list()
        for y in range(len(image[0])):
            image_channel_values.append(get_pixel_channel_values(image, x, y))
        image_list.append(image_channel_values)
    return tuple(image_list)
