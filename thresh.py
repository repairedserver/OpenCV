import cv2 as cv

img = cv.imread('Images/iphone.jpg')
cv.imshow('Photo', img)

cv.waitKey(0)