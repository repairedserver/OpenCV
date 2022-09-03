# OpenCV-Python 정리

# 1. 개요

- OpenCV는 **Open Source Computer Vision Library**의 약어로 오픈소스 컴퓨터 비전 라이브러리이다.
- 실시간 영상 처리에 중점을 둔 영상 처리 라이브러리로서, Apache 2.0 라이선스하에 배포되어
    
    학술적 용도 외에도 상업적 용도로도 사용할 수 있음.
    
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

![Untitled](OpenCV-Python%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20297c5bbfbeaf478bbbead032f946ee78/Untitled.png)

## 3-5. 이미지 색상 변환

`색상 공간 변환(Convert Color)`은 본래의 색상 공간에서 다른 색상 공간으로 변환할 때 사용함.

```python
import cv2 as cv

src = cv.imread("Image/crow.jpg", cv.IMREAD_COLOR)
dst = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

cv.imshow("src", src)
cv.imshow("dst", dst)
cv.waitKey()
cv.destroyAllWindows()
```

`cv2.cvtcolor()`로 이미지의 색상 공간을 변경할 수 있다.

`dst = cv2.cvtcolor(src, code, dstCn)`는 `입력 이미지(src)`, `색상 변환 코드(code)`, `출력 채널(dstCn)`으로 `출력 이미지(dst)`을 생성함.

`색상 변환 코드`는 `원본 이미지 색상 공간`**2**`결과 이미지 색상 공간`을 의미.

`원본 이미지 색상 공간`은 `원본 이미지`와 일치해야 함.

`출력 채널`은 출력 이미지에 필요한 채널의 수를 설정.

- `BGR`은 `RGB` 색상 채널을 의미. (Byte 역순)
- 출력 채널은 기본값을 사용하여 자동으로 채널의 수를 결정.

[채널 범위](https://www.notion.so/eb10f7e757b24f4cadb19b4550a8023f)

[색상 공간 코드](https://www.notion.so/0ff8e8992a5a45f287f335c1e48652d2)

예)`BGR2GRAY`는 `Blue, Green, Red 채널` 이미지를 `단일 채널, 그레이스케일` 이미지로 변경.

![Untitled](OpenCV-Python%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20297c5bbfbeaf478bbbead032f946ee78/Untitled%201.png)

## 3-6. 이진화

`이진화(Binary)`는 어느 지점을 기준으로 값이 높거나 낮은 픽셀의 값을 대상으로 특정 연산을 수행할 때 사용.

일반적으로 값이 높거나 낮은 픽셀을 `검은색` 또는 `흰색`의 값으로 변경함.

기준값에 따라 이분법적으로 구분해 픽셀을 **참 또는 거짓으로 나누는 연산**이며, 이미지 행렬에서 모든 픽셀에 대해 연산이 수행됨.

```python
import cv2 as cv

src = cv.imread("Image/geese.jpg", cv.IMREAD_COLOR)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv.imshow("dst", dst)
cv.waitKey()
cv.destroyAllWindows()
```

`retval, dst = cv2.threshold(src, thresh, maxval, type)`는 `입력 이미지(src)`를 

`임곗값 형식(type)`에 따라 `임곗값(thresh)`과 `최댓값(maxval)`을 활용하여 

`설정 임곗값(retval)`과 `결과 이미지(dst)`를 반환.

---

`입력 이미지`는 단일 채널 이미지(그레이스케일)을 입력해 사용함.

`임곗값 형식`은 `임곗값`을 초과한 값은 `최댓값`으로 변경하고 `임곗값` 이하의 값은 `0`으로 바꾸는 등의 연산을 적용.

---

`설정 임곗값`은 일반적으로 `임곗값`과 동일하지만, 임곗값을 대신 계산해주는 알고리즘인 `Otsu`나 `Triangle`를 사용한다면, 해당 알고리즘에서 계산해준 `임곗값`을 알 수 있음.

예시에서는 임곗값을 **100**, 최댓값을 **255**, 임곗값 형식을 `cv2.THRESH_BINARY`로 사용하였으므로, 픽셀의 값이 100을 초과하는 경우에는 255의 값으로 변경되며, 100 이하의 값은 0으로 변경됨.

---

수식으로 표현한다면 dst=( src > thresh ) ? maxval:0 으로 표현할 수 있다.

- Tip : 다중 채널 이미지를 입력 이미지로 사용하였을 때, 각 채널마다 이미지를 분리해 이진화 연산을 적용.

[임계값 형식](https://www.notion.so/19020019ac344df8997a2f208c2db64a)

![Untitled](OpenCV-Python%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20297c5bbfbeaf478bbbead032f946ee78/Untitled%202.png)

![Untitled](OpenCV-Python%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20297c5bbfbeaf478bbbead032f946ee78/Untitled%203.png)

## 3-7. 흐림 효과

![Untitled](OpenCV-Python%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20297c5bbfbeaf478bbbead032f946ee78/Untitled%204.png)

`흐림 효과(Blur)`는 **블러링(Blurring)** 또는 **스무딩(Smoothing)**이라 불리며, 노이즈를 줄이거나 외부 영향을 최소화하는 데 사용됨.

흐림 효과는 영상이나 이미지를 번지게 하며, 해당 픽셀의 주변 값들과 비교하고 계산해서 픽셀들의 색상을 재조정함.

단순히 이미지를 흐리게 만드는 것뿐만 아니라 **노이즈를 제거해서 연산 시 계산을 빠르고 정확하게 수행하는 데 도움을 줌.**

```python
import cv2 as cv

src = cv.imread("Image/geese.jpg", cv.IMREAD_COLOR)
dst = cv.blur(src, (9, 9), anchor=(-1, -1), borderType=cv.BORDER_DEFAULT)

cv.imshow("dst", dst)
cv.waitKey()
cv.destroyAllWindows()
```

`cv2.blur()`로 입력 이미지에 흐림 효과를 적용할 수 있습니다.

단순 흐림 효과는 각 픽셀에 대해 커널을 적용해 모든 픽셀의 단순 평균을 구하는 연산이다.

`dst = cv2.blur(src, ksize, anchor, borderType)`는 `입력 이미지(src)`를 `커널 크기(ksize)`, `고정점(anchor)`, `테두리 외삽법(borderType)`으로 흐림 효과를 적용한 `결과 이미지(dst)`를 반환.

커널, 고정점, 테두리 외삽법에 대한 내용은 다음과 같음.

### 커널(Kernel)

![Untitled](OpenCV-Python%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5%20297c5bbfbeaf478bbbead032f946ee78/Untitled%205.png)

`커널(kernel)`은 이미지에서 **(x, y)의 픽셀과 해당 픽셀 주변을 포함한 작은 크기의 공간**을 의미함.

이 영역 각각의 특정한 수식이나 함수 등을 적용해 새로운 이미지를 얻는 알고리즘에서 사용.

커널은 영역의 형태와 요소가 결합되는 방식을 정의하는 템플릿을 의미하기도 하며, 신호 처리 분야에서는 커널을 `필터(filter)`라고도 함.

위 이미지의 파란색 사각형 내부가 **커널**이 되며, 파란색 사각형 크기가 `3 x 3`이므로, 커널의 크기는 `3 x 3`이다.

### **고정점(Anchor Point)**

`고정점(Anchor Point)`은 커널을 통해 컨벌루션된 값을 할당한 지점.

여기서 `컨벌루션(Convolution)`이란 **새로운 픽셀**을 만들어 내기 위해 `커널 크기의 화소 값을 이용해 어떤 시스템을 통과해 계산하는 것`을 의미.

커널 내에서 고정점은 하나의 지점만을 가지며, 이미지와 어떻게 정렬되는지를 나타냄.

위 이미지의 빨간색 부분이 **고정점**이 되며, 빨간색 사각형의 위치는 파란색 사각형을 기준으로 `(1, 1)`에 위치.

### **테두리 외삽법(Border Extrapolation)**

`테두리 외삽법(Border Extrapolation)`은 컨벌루션을 적용할 때, **이미지 가장자리 부분의 처리 방식**을 의미.

컨벌루션을 적용하면 이미지 가장자리 부분은 계산이 불가능한데, 이 문제를 해결하기 위해 테두리의 이미지 바깥쪽에 `가상의 픽셀`을 만들어 처리함.

가상 픽셀의 값을 **0으로 처리**하거나, **임의의 값**을 할당하거나, **커널이 연산할 수 있는 부분부터** 연산을 수행하기도 함.

예를 들어 `cv2.BORDER_DEFAULT`는 `gfedcb | abcdefgh | gfedcba`의 형태로 외삽을 진행하는데 `abcdefgh`는 픽셀의 값을 의미.

즉 테두리 부분이 a라면 테두리 밖의 부분은 이미지를 반사하듯이 표현되어, `gfedcb`나 `gfedcba`의 형태로 할당됨.

위 이미지의 굵은 선 바깥 부분에 대해 **테두리 외삽법**이 적용됨.

[픽셀 외삽법 종류](https://www.notion.so/85aa496f7e034f8588d6dcbbcc99b080)

## 3-7. 이미지 가장자리 검출

`가장자리(Edge)`는 가장 바깥 부분의 둘레를 의미하며, 객체의 테두리로 볼 수 있다.

이미지 상에서 가장자리는 `전경(Foreground)`과 `배경(Background)`이 구분되는 지점이며, 전경과 배경 사이에서 **밝기가 큰 폭으로 변하는 지점**이 객체의 가장자리가 된다.

가장자리를 찾기 위해 **미분(Derivative)**과 **기울기(Gradient)** 연산을 수행하며, 이미지 상에서 픽셀의 밝기 변화율이 높은 경계선을 찾는다.

```python
import cv2 as cv

src = cv.imread("Image/wheat.jpg", cv.IMREAD_COLOR)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

sobel = cv.Sobel(gray, cv.CV_8U, 1, 0, 3)
laplacian = cv.Laplacian(gray, cv.CV_8U, ksize=3)
canny = cv.Canny(src, 100, 255)

cv.imshow("sobel", sobel)
cv.imshow("laplacian", laplacian)
cv.imshow("canny", canny)
cv.waitKey()
cv.destroyAllWindows()
```

```python
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
```

`소벨 함수(cv2.Sobel)`로 입력 이미지에서 가장자리를 검출할 수 있다.

미분 값을 구할 때 가장 많이 사용되는 연산자이며, 인접한 픽셀들의 차이로 **기울기(Gradient)의 크기**를 구함.

이때 인접한 픽셀들의 기울기를 계산하기 위해 컨벌루션 연산을 수행.

`dst = cv2.Sobel(src, ddepth, dx, dy, ksize, scale, delta, borderType)`은 `입력 이미지(src)`에 

`출력 이미지 정밀도(ddepth)`를 설정하고 `dx(X 방향 미분 차수)`, `dy(Y 방향 미분 차수)`, `커널 크기(ksize)`, 

`비율(scale)`, `오프셋(delta)`, `테두리 외삽법(borderType)`을 설정하여 `결과 이미지(dst)`를 반환한다.

---

`출력 이미지 정밀도`는 반환되는 결과 이미지의 정밀도를 설정.

`X 방향 미분 차수`는 이미지에서 `X 방향`으로 미분할 차수를 설정.

`Y 방향 미분 차수`는 이미지에서 `Y 방향`으로 미분할 차수를 설정.

`커널 크기`는 소벨 마스크의 크기를 설정합니다. `1`, `3`, `5`, `7` 등의 홀수 값을 사용하며, **최대 31**까지 설정할 수 있다.

`비율`과 `오프셋`은 출력 이미지를 반환하기 전에 적용되며, 주로 시각적으로 확인하기 위해 사용함.

`픽셀 외삽법`은 이미지 가장자리 부분의 처리 방식을 설정.

- `X 방향 미분 차수`와 `Y 방향 미분 차수`는 합이 1 이상이여야 하며, 0의 값은 해당 방향으로 미분하지 않음을 의미.

---

```python
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
```

`라플라시안 함수(cv2.Laplacian)`로 입력 이미지에서 가장자리를 검출할 수 있다.

라플라시안은 2차 미분의 형태로 가장자리가 밝은 부분에서 발생한 것인지, 어두운 부분에서 발생한 것인지 알 수 있음.

2차 미분 방식은 X 축과 Y 축을 따라 2차 미분한 합을 의미합니다.

`dst = cv2.laplacian(src, ddepth, ksize, scale, delta, borderType)`은 `입력 이미지(src)`에 

`출력 이미지 정밀도(ddepth)`를 설정하고 `커널 크기(ksize)`, `비율(scale)`, `오프셋(delta)`, 

`테두리 외삽법(borderType)`을 설정하여 `결과 이미지(dst)`를 반환한다.

`출력 이미지 정밀도`는 반환되는 결과 이미지의 정밀도를 설정함.

`커널 크기`는 라플라시안 필터의 크기를 설정합니다. `커널`의 값이 1일 경우, **중심값이 -4인 3 x 3 Aperture Size**를 사용.

`비율`과 `오프셋`은 출력 이미지를 반환하기 전에 적용되며, 주로 시각적으로 확인하기 위해 사용.

`픽셀 외삽법`은 이미지 가장자리 부분의 처리 방식을 설정함.