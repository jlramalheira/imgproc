# coding=utf-8
import numpy as np
import cv2
import sys
sys.path.insert(0, '../src')
import main


img = cv2.imread(sys.argv[1], 0)
img = main.invert_image(img)
img = np.tile(img, (2, 3))
height, width = img.shape
grad = main.create_diagonal_gradient(height, width)
result = main.bland(img, grad)

cv2.imshow('img', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
