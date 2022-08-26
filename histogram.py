import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Images/iphone.jpg')
cv.imshow('image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayimage', gray)

# Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# 픽셀 분포
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)