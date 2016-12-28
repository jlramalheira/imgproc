import numpy as np
import cv2
import sys
from collections import deque
from scipy import *
sys.path.insert(0, '../src')
import main


def findPoints(imgBorder):
    q = deque()
    domain = []
    ranges = []
    points = np.where(imgBorder == 255)
    x = points[0][0]
    y = points[1][0]
    q.append((x, y))
    while len(q) > 0:
        u = q.popleft()
        x = u[0]
        y = u[1]
        domain.append(x)
        ranges.append(y)
        imgBorder[x, y] = 0
        if x > 0 and imgBorder[x - 1][y] == 255:
            q.append((x - 1, y))
        if x < (width - 1) and imgBorder[x + 1][y] == 255:
            q.append((x + 1, y))
        if y > 0 and imgBorder[x][y - 1] == 255:
            q.append((x, y - 1))
        if y < (height - 1) and imgBorder[x][y + 1] == 255:
            q.append((x, y + 1))
    return domain, ranges


img = cv2.imread(sys.argv[1], 0)
cv2.imshow('ImageIn', img)
height, width = img.shape

imgBin = (np.uint8)(img >= 127) * 255

kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(imgBin, kernel, iterations = 1)
imgBorder = imgBin - erosion
cv2.imshow('Border', imgBorder)

domain, ranges = findPoints(imgBorder)
complexArray = np.array(domain).astype(complex)
complexArray.imag = np.array(ranges)

fourierTransform = np.fft.fft(complexArray)

limitDescritors = int(sys.argv[2])
fourierTransform[limitDescritors:] = 0

fourierInverse = np.fft.ifft(fourierTransform)

xCoordenates = np.real(fourierInverse).astype(int)
yCoordenates = np.imag(fourierInverse).astype(int)

imgResult = np.zeros((height, width), np.uint8)
imgResult[xCoordenates, yCoordenates] = 255

cv2.imshow('Result', imgResult)

cv2.waitKey(0)
cv2.destroyAllWindows()
