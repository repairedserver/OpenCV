import cv2 as cv
import numpy as np

img = cv.imread('Images/iphone.jpg')
cv.imshow('Pic', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# laplaction
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplaction', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel_X', sobelx)
cv.imshow('Sobel_Y', sobely)
cv.imshow('Combined_Sobel', combined)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)