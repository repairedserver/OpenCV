import cv2 as cv

image = cv.imread('Images/dogeJPG.jpg')
video = cv.VideoCapture('Videos/LotteBigbar.mp4')
cv.imshow('Doge', image)

 # 파일의 크기를 축소시키는 함수
def rescaleFile(frame, scale=0.75):
    width = int(frame.shape[1] * scale) # 너비를 25% 줄임 (너비 x 0.75)
    height = int(frame.shape[0] * scale) # 높이를 25% 줄임 (높이 x 0.75)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    # cv.INTER_AREA: 영역적인 정보를 추출해 결과 영상을 셋팅하며 영상 축소에 효과적

resized_image = rescaleFile(image)
cv.imshow('Resized Doge', resized_image)

def changeRes(width, height):
    # 이미 존재하는 비디오 파일에선 실행되지 않음
    # 그래서 라이브 비디오의 해상도를 변경하려는 경우에서 사용됨
    video.set(3, width)
    video.set(4, height)

while True:
    isTrue, frame = video.read()
    frame_resized = rescaleFile(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()