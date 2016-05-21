# coding=utf-8
import numpy as np
import cv2


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
