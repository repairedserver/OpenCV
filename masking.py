import cv2 as cv
import numpy as np

img = cv.imread('Images/dogeJPG.jpg')
cv.imshow('Dog', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank, (img.shape[1]//2 - 180, img.shape[0]//2 - 105), 100, 255, -1)
cv.imshow('MaskDog', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('MaskedDog', masked)
cv.waitKey(0)