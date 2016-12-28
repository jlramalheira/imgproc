# coding=utf-8
import numpy as np
import cv2
import sys

def create_diagonal_gradient(height, width):
    rows = np.arange(height)
    cols = np.arange(width)
    rows, cols = np.meshgrid(rows, cols, indexing='ij')
    grad = rows*cols
    grad = grad / (grad.max() / 255)
    return grad


def blend(img1, img2):
    img = (np.uint8)((img1 + img2) / 2)
    return img

img = cv2.imread(sys.argv[1], 0)
img = img[::-1, ::-1]
img = np.tile(img, (2, 3))
height, width = img.shape
grad = create_diagonal_gradient(height, width)
result = blend(img, grad)

cv2.imshow('img', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
