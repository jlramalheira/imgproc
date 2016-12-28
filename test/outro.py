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
        if y > 0:
            if imgBorder[x][y - 1] == 255:
                q.append((x, y - 1))
            elif x < (width - 1) and imgBorder[x + 1][y - 1] == 255:
                q.append((x + 1, y - 1))
        elif x < (width - 1):
            if imgBorder[x + 1][y] == 255:
                q.append((x + 1, y))
            elif y < (height - 1) and imgBorder[x + 1][y + 1] == 255:
                q.append((x + 1, y + 1))
        elif y < (width - 1):
            if imgBorder[x][y + 1] == 255:
                q.append((x, y + 1))
            elif x > 0 and imgBorder[x - 1][y + 1] == 255:
                q.append((x - 1, y + 1))
        elif x > 0:
            if imgBorder[x - 1][y] == 255:
                q.append((x - 1, y))
            elif y > 0 and imgBorder[x - 1][y - 1] == 255:
                q.append((x - 1, y - 1))
    return domain, ranges


img = cv2.imread(sys.argv[1], 0)
cv2.imshow('ImageIn', img)
height, width = img.shape

imgBin = (np.uint8)(img >= 127) * 255

# kernel = np.ones((3, 3), np.uint8)
kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
erosion = cv2.erode(imgBin, kernel, iterations = 1)
imgBorder = imgBin - erosion
cv2.imshow('Border', imgBorder)

domain, ranges = findPoints(imgBorder)
complexArray = np.array(domain).astype(complex)
complexArray.imag = np.array(ranges)

fourierTransform = np.fft.fft(complexArray)

limitDescritors = int(sys.argv[2])
# fourierTransform[limitDescritors:] = 0

fourierInverse = np.fft.ifft(fourierTransform)

xCoordenates = np.real(fourierInverse)
xCoordenates = xCoordenates + 0.5
xCoordenates = xCoordenates.astype(np.uint16)
yCoordenates = np.imag(fourierInverse)
yCoordenates = yCoordenates + 0.5
yCoordenates = yCoordenates.astype(np.uint16)

imgResult = np.zeros((height, width), np.uint8)
imgResult[xCoordenates, yCoordenates] = 255

cv2.imshow('Result', imgResult)

cv2.waitKey(0)
cv2.destroyAllWindows()
