import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') # 500x500 넓이의 이미지를 공백으로 채우고 3채널
#uint8은 기본적인 이미지 데이터 유형
cv.imshow('Blank', blank)

# blank[200:300, 300:400] = 0, 255, 0 #B G R 값에서 G(Green)에만 값을 넣음
# cv.imshow('Color', blank)

cv.rectangle(blank, (0,0),(255,255),(0,255,0), thickness=2) #(0,0) 좌표에서 (255,255)까지, 초록색(0,255,0)으로 두께(thickness)는 2픽셀의 직사각형
# thickness=cv.FILLED 라면 사각형을 모두 채움
# thickness=음수라면 면을 전부 채움
cv.imshow('GreenRectangle', blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
#반지름 40픽셀의 빨간색(0, 0, 255) 원
cv.imshow('RedCircle', blank)

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
#하얀색의 (0,0)으로 향하는 직선
cv.imshow('WhiteLine', blank)

cv.putText(blank, 'Hello World', (255, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 0), 2)
#하늘색의 (255, 255)에서 시작하는 텍스트
cv.imshow('Text', blank)
cv.waitKey(0)