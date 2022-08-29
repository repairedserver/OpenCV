import cv2 as cv

img = cv.imread('Faces/jammin.jpeg')
cv.imshow('Jammin', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayJammin', gray)

cv.waitKey(0)