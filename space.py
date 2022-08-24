import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Images/dogeJPG.jpg')
cv.imshow('Dog', img)

plt.imshow(img)
plt.show()

'''
CV와 matplotlib에서 실행 이미지를 보면 완전히 다른데
그 이유는 이미지가 BGR 이미지이기 때문 (matplotlib은 RGB로 표시함)
'''

# # BGR -> Gray
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('GrayDog', gray)

# BGR -> HSV (색Hue, 채도Saturation, 명도Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV_Dog', hsv)

# # BGR -> LAB
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB_Dog', lab)

# BGR -> RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB_Dog', rgb)

# HSV -> BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('BGR_ReturnDog', hsv_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)