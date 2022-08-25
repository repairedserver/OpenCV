import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# 비트연산 AND
bitwiseAND = cv.bitwise_and(rectangle, circle) # 두 이미지의 교차 영역만을 반환
cv.imshow('BitwiseAND', bitwiseAND)

# 비트연산 OR
bitwiseOR = cv.bitwise_or(rectangle, circle) # 교차 영역과 그렇지 않은 부분도 모두 반환
cv.imshow('BitwiseOR', bitwiseOR)

# 비트연산 XOR
bitwiseXOR = cv.bitwise_xor(rectangle, circle) # 교차 영역을 제외한 모두를 반환
cv.imshow('BitwiseXOR', bitwiseXOR)

# 비트연산 NOT
bitwiseNOT = cv.bitwise_not(rectangle) # 색상 반전
cv.imshow('BitwiseNOT', bitwiseNOT)
cv.waitKey(0)