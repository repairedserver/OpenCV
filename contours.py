import cv2 as cv

img = cv.imread('Images/dogePNG.png')
cv.imshow('Doge', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayDog', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('BlurDog', blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('CannyDog', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('ThreshDog', thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)