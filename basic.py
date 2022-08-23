import cv2 as cv

img = cv.imread('Images/dogeJPG.jpg')
cv.imshow('Dog', img) #현재는 3채널 BGR 이미지

#이미지를 흑백(grayscale)으로 변경
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayDog', gray)

#이미지를 블러(Blur) 처리
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #커널 사이즈는 기본적으로 홀수로 설정
cv.imshow('BlurDog', blur)

#이미지의 가장자리 추출
canny = cv.Canny(img, 125, 175)
cv.imshow('CannyDog', canny)

#확대 이미지
dilated = cv.dilate(canny, (7,7), iterations=1) # 가장자리만 추출된 이미지의 가장자리를 확대시킴
cv.imshow('DilatedDog', dilated)
cv.waitKey(0)