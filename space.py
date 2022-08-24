import cv2 as cv

img = cv.imread('Images/dogeJPG.jpg')
cv.imshow('Dog', img)

#BGR -> Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayDog', gray)
cv.waitKey(0)