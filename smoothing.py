import cv2 as cv

img = cv.imread('Images/dogeJPG.jpg')
cv.imshow('Dog', img)

# 평균화 (이미지의 특정 부분에 대해 커널 정의)
average = cv.blur(img, (7,7))
cv.imshow('AverageBlurDog', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('GaussBlurDog', gauss)

# 중앙값 흐림 (Median Blur)
median = cv.medianBlur(img, 7) # 이 커널의 크기는 튜플이 아닌 그냥 정수(자동으로 설정됨)
cv.imshow('MedianBlurDog', median)

# Bilaterial
bilaterial = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('BilaterialDog', bilaterial)
cv.waitKey(0)