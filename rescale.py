import cv2 as cv

image = cv.imread('Images/dogeJPG.jpg')
video = cv.VideoCapture('Videos/LotteBigbar.mp4')
cv.imshow('Doge', image)

def rescaleFile(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFile(image)
cv.imshow('Resized Doge', resized_image)
while True:
    isTrue, frame = video.read()
    frame_resized = rescaleFile(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()