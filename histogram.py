import cv2 as cv

img = cv.imread('Images/rtx3090ti.jpg')
cv.imshow('RTX', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayRTX', gray)
cv.waitKey(0)