import cv2




def read_img(path: str):
    # Reads an image into GRAYSCALE [0-255]
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('test', image)
    cv2.waitKey(0)
    image = cv2.resize(image, (64, 64))
    return image
