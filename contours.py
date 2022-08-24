import cv2 as cv

img = cv.imread('Images/dogePNG.png')
cv.imshow('Doge', img)

cv.waitKey(0)