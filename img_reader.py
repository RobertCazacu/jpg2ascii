import cv2




def read_img(path):
    # Reads an image into GRAYSCALE [0-255]
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return image
