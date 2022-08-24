import cv2 as cv
import numpy as np

img = cv.imread('Images/dogeJPG.jpg')
cv.imshow('Dog', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
b, g, r = cv.split(img) # 각 색깔을 밝은색으로 강조

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('BlueDog', blue)
cv.imshow('GreenDog', green)
cv.imshow('RedDog', red)

# print(img.shape) # 채널의 수가 3인 이유는 각 색깔(RGB)이 3개이기 때문
# print(b.shape)
# print(g.shape)
# print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow('MergeDog', merged)
cv.waitKey(0)