import cv2 as cv

img = cv.imread('Images/iphone.jpg')
cv.imshow('Photo', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayPic', gray)

# 간단한 임계값 (Simple Thresholding)
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('SimpleThreshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('SimpleThresholdINV', thresh_inv)

# 적응형 임계값 (Adaptive Thresholding)
adapt_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
cv.THRESH_BINARY, 9, 3)
cv.imshow('AdaptThresholding', adapt_thresh)
cv.waitKey(0)