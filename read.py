import cv2 as cv #opencv 라이브러리 

#  reading image
'''
doge = cv.imread('Images/dogeJPG.jpg') # 이미지의 대한 경로를 가져옴
# 이미지를 픽셀 행렬로 읽어들임
cv.imshow('Dog', doge) # 읽은 이미지를 'Dog'란 이름의 창으로 출력
'''

# reading video
bigbar = cv.VideoCapture('Videos/LotteBigbar.mp4') #비디오 경로를 가져옴
#cv.VideoCapture 메서드는 0123같은 정수 인수 또는 비디오파일 경로를 취함
# ex) 0 : 웹캠, 1 : 연결된 첫 번째 카메라, 2 : 연결된 두번째 카메라---

#opencv는 프레임 단위로 비디오를 읽음 = 소리는 안나옴
while True:
    isTrue, frame = bigbar.read() #isTrue: 프레임이 성공적으로 읽힌 여부를 나타내는 불 대수
    # .read() 메서드는 비디오에서 프레임 단위로 읽고 반환
    cv.imshow('Bigbar.mp4', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): # 'd' 키를 누른다면 비디오 읽기 중지
        break

bigbar.release()
cv.destroyAllWindows() # 모든 창 닫음

#cv.waitKey(0) # 특정 지연 또는 키를 누를 때까지의 시간(ms) 대기
# 0은 무한 대기