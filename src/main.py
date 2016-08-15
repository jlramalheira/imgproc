# coding=utf-8
import numpy as np
import cv2

def gamma_correction(img, gamma):
    lut = (((np.arange(256, dtype=np.float32) / 255) ** gamma) * 255).astype(np.uint8)
    result = lut[img]
    return result


def invert_image(img):
    return img[::-1, ::-1]


def create_diagonal_gradient(height, width):
    rows = np.arange(height)
    cols = np.arange(width)
    rows, cols = np.meshgrid(rows, cols, indexing='ij')
    grad = rows*cols
    grad = grad / (grad.max() / 255)
    return grad


def bland(img1, img2):
    img = (np.uint8)((img1 + img2) / 2)
    return img

def hsv_disc(size=512):
    disc = np.zeros([size, size, 3])
    (x, y, z) = np.indices(disc)
    row_indexes = x - (size / 2)
    col_indexes = y - (size / 2)
    disc[1] = np.arctan2(col_indexes, row_indexes)
    return disc;
