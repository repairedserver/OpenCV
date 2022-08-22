import cv2 as cv

#  reading image
'''
doge = cv.imread('Images/dogeJPG.jpg')
cv.imshow('Dog', doge)
'''

# reading video
bigbar = cv.VideoCapture('Videos/LotteBigbar.mp4')

while True:
    isTrue, frame = bigbar.read()
    cv.imshow('Bigbar.mp4', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

bigbar.release()
cv.destroyAllWindows()
#cv.waitKey(0)