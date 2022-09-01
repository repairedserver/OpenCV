# OpenCV-Python 정리

# 1. 개요

- OpenCV는 **Open Source Computer Vision Library**의 약어로 오픈소스 컴퓨터 비전 라이브러리이다.
- 실시간 영상 처리에 중점을 둔 영상 처리 라이브러리로서, Apache 2.0 라이선스하에 배포되어
    
    학술적 용도 외에도 상업적 용도로도 사용할 수 있습니다.
    
- 물체인식, 얼굴인식, 제스처인식을 비롯해 자율주행 자동차, OCR 판독기, 불량 검사기 등에 활용

# 2. 세팅

**파이썬 터미널을 켜서 아래 라이브러리 설치**

```python
**pip install opencv-python
pip install opencv-contrib-python
pip install opencv-python-headless
pip install opencv-contrib-python-headless**
```

`contrib`이 포함된 패키지는 확장 모듈이 포함된 패키지

`headless`가 포함된 패키지는 서버 환경(Docker, Cloud)에서 사용할수 있는 OpenCV

**잘 설치되었는지 확인**

```python
import cv2 as cv
print(cv.__version__)

# 결과로 opencv의 버전인 4.6.0이 나옴
```

# 3. 사용

## 3-1. 이미지 불러오기

```python
import cv2 as cv
img = cv.imread('Image/image.jpg')
# 파일의 확장자를 맞게 해줘야 불러와짐

cv.imshow('Picture', img) # Picture라는 이름으로 이미지 출력
cv.waitKey(0) # 아무 키를 누를때까지 대기 (0은 무한대기)
```

## 3-2. 카메라를 사용해보기

OpenCV로 카메라 출력을 사용할 수 있다.

카메라 출력은 카메라가 스트리밍 형태로 동작할때 사용 가능하다

```python
import cv2 as cv

capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

while cv.waitKey(33) < 0:
    ret, frame = capture.read()
    cv.imshow("VideoFrame", frame)

capture.release()
cv.destroyAllWindows()
```

`비디오 출력 클래스(cv.VideoCapture)`를 통해 **내장** 또는 **외장 카메라**에서 정보를 받아올 수 있다.

`cv.VideoCapture(index)`로 카메라와 연결함. `index`는 **카메라의 장치 번호**를 의미합니다.

노트북의 경우, 일반적으로 내장 카메라가 존재하므로 노트북 카메라의 장치 번호는 `0`이 됨.

추가적으로 **외장 카메라**를 사용하는 경우, 장치 번호가 `1~n`까지 순차적으로 할당됨.

---

`capture.set()`로 카메라의 속성을 설정.

`capture.set(propid, value)`로 카메라의 `속성(propid)`과 `값(value)`을 설정할 수 있음.

`propid`은 변경하려는 **카메라 설정**을 의미.

`value`은 변경하려는 **카메라 설정의 속성값**을 의미.

예시는 카메라의 넓이는 640, 높이는 480으로 640x480의 해상도가 설정됨

---

`반복문(While)`을 활용하여 카메라에서 프레임을 지속적으로 받아옴.

`cv.waitkey()`는 지정된 시간 동안 키 입력이 있을 때까지 프로그램을 지연시킴.

`cv.waitkey(delay)`로 키 입력을 기다립니다. `delay(ms)`는 **지연 시간**을 의미함.

키 입력 대기 함수는 입력된 키의 **아스키 코드 값**을 반환함.

= 어떤 키라도 입력되기 전까지 33ms마다 반복문을 실행.

- `delay`가 **0**일 경우, 지속적으로 키 입력을 검사하여 프레임이 넘어가지 않음**(무한 대기).**
- `while cv2.waitKey(33) != ord('q'):`으로 사용할 경우, `q`가 입력될 때 반복문을 종료함.

---

`capture.relase()`로 카메라 장치에서 받아온 메모리를 해제.

`cv.destroyAllWindows()`를 이용하여 모든 윈도우 창을 닫음.

## 3-3. 비디오 출력하기

```python
import cv2 as cv

capture = cv.VideoCapture("Image/Star.mp4")

while cv.waitKey(33) < 0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = capture.read()
    cv.imshow("VideoFrame", frame)

capture.release()
cv.destroyAllWindows()
```

`cv2.VideoCapture()`를 통해 **동영상 파일**에서 정보를 받아올 수 있다.

`capture = cv2.VideoCapture(fileName)`는 `파일 경로(fileName)`의 동영상 파일을 불러옴.

---

`capture.get()`로 비디오의 속성을 반환함.

비디오의 정보 중, `현재 프레임 수(cv2.CAP_PROP_POS_FRAMES)`와 `총 프레임 수(cv2.CAP_PROP_FRAME_COUNT)`를 받아옴.

`if`을 이용하여 `동영상의 현재 프레임 수`와 `동영상의 총 프레임 수`를 비교.

현재 프레임의 수가 총 프레임 수가 같다면, 현재 재생되고 있는 프레임은 가장 마지막이 됨.

[VideoCapture 메서드](https://www.notion.so/f6a87d830565444eb76bc4faff151178)

[VideoCapture 속성](https://www.notion.so/a49db9a2c3cc490f86efbcc935415abb)

## 3-4. 이미지 회전

2차원 공간에서의 회전은 크게 **좌푯값을 회전**시키는 것과 **좌표 축을 회전**시키는 것이 있다.

좌푯값 회전은 원점을 중심으로 회전시키며, 좌표 축 회전은 원점을 중심으로 행렬 자체를 회전시킴.

```python
import cv2 as cv

src = cv.imread("Image/ara.jpg", cv.IMREAD_COLOR)

height, width, channel = src.shape
matrix = cv.getRotationMatrix2D((width/2, height/2), 90, 1)
dst = cv.warpAffine(src, matrix, (width, height))

cv.imshow("src", src)
cv.imshow("dst", dst)
cv.waitKey()
cv.destroyAllWindows()
```

`height, width, channel = src.shape`를 이용하여 해당 이미지의 `높이`, `너비`, `채널`의 값을 저장.

`높이`와 `너비`를 이용하여 **회전 중심점**을 설정함.

---

`cv.getRotationMatrix2D()`로 회전 변환 행렬을 계산함.

`matrix = cv.getRotationMatrix2D(center, angle, scale)`는 `중심점(center)`, `각도(angle)`, `비율(scale)`로 `매핑 변환 행렬(matrix)`을 생성합니다.

`중심점(center)`은 `튜플(Tuple)` 형태로 사용하며 회전의 **기준점**을 설정합니다.

`각도(angle)`는 중심점을 기준으로 **회전할 각도**를 설정합니다.

`비율(scale)`은 이미지의 **확대 및 축소 비율**을 설정합니다.

---

`cv.warpAffine()`로 회전 변환을 계산합니다.

`dst = cv2.warpAffine(src, M, dsize)`는 `원본 이미지(src)`에 `M(아핀 맵 행렬)`을 적용하고 

`출력 이미지 크기(dsize)`로 변형해서 `출력 이미지(dst)`를 반환.

`아핀 맵 행렬(M)`은 회전 행렬 생성 함수에서 반환된 매핑 변환 행렬을 사용.

`출력 이미지 크기(dsize)`는 `튜플(Tuple)` 형태로 사용하며 출력 이미지의 너비와 높이를 의미함.

`아핀 맵 행렬`에 따라 `회전된 이미지`를 반환.