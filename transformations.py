import cv2 as cv
import numpy as np

img = cv.imread('Images/dogeJPG.jpg')
cv.imshow('Doge', img)

# 이미지 이동
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimentions)

# -x -> Left
# -y -> Up
# x -> Right
# y -> Down

translated = translate(img, 100, 100) # 이미지를 오른쪽으로 100칸 아래로 100칸
cv.imshow('TranslatedDoge', translated)

# 이미지 회전
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None: # 설정된 회전점이 없으면 중심으로 회전한다 가정
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width, height)

    return cv.warpAffine(img, rotMat, dimentions)

rotated = rotate(img, 45) # 오른쪽으로 45도 회전
cv.imshow('SpinDoge', rotated)

rotated_rotated = rotate(rotated, -45) # 다시 왼쪽으로 45도 회전
cv.imshow('SpinReturnDoge', rotated_rotated)

# 크기 조정
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('ResizeDoge', resized)

# 뒤집기
fliped = cv.flip(img, 0)
cv.imshow('FlipDoge', fliped)
cv.waitKey(0)