import numpy as np
import cv2
import sys
from collections import deque

def find_neighbors(x, y, height, width, color, img):
    q = deque()
    q.append((x, y))
    while len(q) > 0:
        u = q.popleft()
        x = u[0]
        y = u[1]
        if img[x, y] == 255:
	    # verificar vizinhos
            if x > 0 and img[x - 1][y] == 255:
                q.append((x - 1, y))
            if x < (width - 1) and img[x + 1][y] == 255:
                q.append((x + 1, y))
            if y > 0 and img[x][y - 1] == 255:
                q.append((x, y - 1))
            if y < (height - 1) and img[x][y + 1] == 255:
                q.append((x, y + 1))
        img[x][y] = color
    return img

img = cv2.imread(sys.argv[1], 0)
height, width = img.shape

imgNeighbors = (np.uint8)(img >= 127) * 255
color = 1
points = np.where(imgNeighbors == 255)
while len(points[0]) > 0:
    x = points[0][0]
    y = points[1][0]
    imgNeighbors = find_neighbors(x, y, height, width, color, imgNeighbors)
    points = np.where(imgNeighbors == 255)
    color += 1

points = np.where(imgNeighbors == int(sys.argv[2]))
if (len(points[0]) > 0):
    mminx = points[0].min()
    mmaxx = points[0].max()
    mminy = points[1].min()
    mmaxy = points[1].max()
    mat = img[mminx:mmaxx, mminy:mmaxy]
    cv2.imshow('origin', img)
    cv2.imshow('img', mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print "Rotulo nao encontrado"
