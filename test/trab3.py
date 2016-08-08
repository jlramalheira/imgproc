import numpy as np
import cv2
import sys


def create_palet():
    red0 = np.random.randint(0, 256)
    red1 = np.random.randint(0, 256)
    green0 = np.random.randint(0, 256)
    green1 = np.random.randint(0, 256)
    blue0 = np.random.randint(0, 256)
    blue1 = np.random.randint(0, 256)

    red = np.linspace(red0, red1, 256)
    green = np.linspace(green0, green1, 256)
    blue = np.linspace(blue0, blue1, 256)

    red = np.uint8(np.tile(red.reshape(256, 1), 256))
    green = np.uint8(np.tile(green.reshape(256, 1), 256))
    blue = np.uint8(np.tile(blue.reshape(256, 1), 256))

    return np.dstack((blue, green, red))

img = cv2.imread(sys.argv[1], 0)
palet = create_palet()
cv2.imshow('palet', palet)

palet = palet[:, 0]

height, width = img.shape
img_out = np.zeros((height, width, 3), dtype=np.uint8)
img_out[::, ::] = palet[img[::, ::]]

cv2.imshow('out', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
