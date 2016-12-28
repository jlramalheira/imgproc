# coding=utf-8
import numpy as np
import cv2
import sys
sys.path.insert(0, '../src')
import main

# GRAY SCALE
img_gray = cv2.imread(sys.argv[1], 0)

result1 = main.gamma_correction(img_gray, 0.5)
result2 = main.gamma_correction(img_gray, 1)
result3 = main.gamma_correction(img_gray, 2)

result = np.hstack((np.hstack((result1, result2)), result3))

cv2.imshow('img_gray', result)
cv2.waitKey(0)

# RGB
img_rgb = cv2.imread(sys.argv[1])

result1 = main.gamma_correction(img_rgb, 0.5)
cv2.imwrite('imagem.png', result1)
result2 = main.gamma_correction(img_rgb, 1)
result3 = main.gamma_correction(img_rgb, 2)

result = np.hstack((np.hstack((result1, result2)), result3))

cv2.imshow('img_rgb', result)
cv2.waitKey(0)

# HSI
img_hsv = cv2.cvtColor(cv2.imread(sys.argv[1]), cv2.COLOR_BGR2HSV)

h = img_hsv[:,:,0]
s = img_hsv[:,:,1]
v = img_hsv[:,:,2]

v1 = main.gamma_correction(v, 0.5)
v2 = main.gamma_correction(v, 1)
v3 = main.gamma_correction(v, 2)

result1 = cv2.cvtColor(np.dstack((h,s,v1)), cv2.COLOR_HSV2BGR)
result2 = cv2.cvtColor(np.dstack((h,s,v2)), cv2.COLOR_HSV2BGR)
result3 = cv2.cvtColor(np.dstack((h,s,v3)), cv2.COLOR_HSV2BGR)

result = np.hstack((np.hstack((result1, result2)), result3))

cv2.imshow('img_hsv', result)
cv2.waitKey(0)

cv2.destroyAllWindows()
