import cv2 as cv

# 개인사진
# img = cv.imread('Faces/yee.jpg')
# cv.imshow('Jammin', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('GrayJammin', gray)


# 단체사진
img = cv.imread('Faces/miss.jpg')
cv.imshow('Miss', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayMiss', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml') 
# XML 코드의 33000줄을 읽고 변수에 저장

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# 해당 이미지의 좌표를 잡고 사각형을 그림
print(f'찾은 얼굴의 수 : {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)
cv.waitKey(0)