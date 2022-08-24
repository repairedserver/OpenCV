from pickletools import uint8
import cv2 as cv
import numpy as np

img = cv.imread('Images/dogePNG.png')
cv.imshow('Doge', img)

blank = np.zeros(img.shape, dtype='uint8') # img랑 크기가 똑같은 공백이미지
cv.imshow('BlankDog', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayDog', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('BlurDog', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('CannyDog', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('ThreshDog', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
#blank 이미지에 contours 테두리를 바탕으로 빨간색의 두께 1로 채움
cv.imshow('ContoursDrawnDog', blank)
# 결과적으로 138개의 윤곽선이 서로의 이미지를 미러링함
cv.waitKey(0)