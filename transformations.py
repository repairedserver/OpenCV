import cv2 as cv
import numpy as np

img = cv.imread('Images/rtx3090ti.jpg')
cv.imshow('RTX', img)

# 이미지 번역
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimentions)

# -x -> Left
# -y -> Up
# x -> Right
# y -> Down

translated = translate(img, 100, 100) # 이미지를 오른쪽으로 100칸 아래로 100칸
cv.imshow('TranslatedRTX', translated)
cv.waitKey(0)