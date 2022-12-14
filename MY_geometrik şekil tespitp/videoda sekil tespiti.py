import cv2
import time
import numpy as np

##################
DELAY = 0.02
USE_CAM = 1
IS_FOUND = 0
url="http://192.168.1.7:8080/shot.jpg"
MORPH = 7
CANNY = 100
##################
# 420x600 oranı 105mmx150mm gerçek boyuttaki kağıt için
_width = 600.0
_height = 420.0
_margin = 0.0
##################
#Programda kullanılacak sabit değişkenleri tanımladık
if USE_CAM: video_capture = cv2.VideoCapture(url)
corners = np.array(
[
[[ _margin, _margin ]],
[[ _margin, _height + _margin ]],
[[ _width + _margin, _height + _margin ]],
[[ _width + _margin, _margin ]],
]
)

pts_dst = np.array( corners, np.float32 )

while True :
    if USE_CAM:
        video_capture = cv2.VideoCapture(url)
        ret, rgb = video_capture.read()  # Kameradan okuyoruz.
    else:
        ret = 1
        rgb = cv2.imread("opencv.jpg", 1)
    if (ret):
        gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

        gray = cv2.bilateralFilter(gray, 1, 10, 120)

        edges = cv2.Canny(gray, 10, CANNY)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (MORPH, MORPH))

        closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        contours, h = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cont in contours:
            if cv2.contourArea(cont) > 5000:
                arc_len = cv2.arcLength(cont, True)
                approx = cv2.approxPolyDP(cont, 0.1 * arc_len, True)  # Yaklaşık olarak köşeleri sayıyoruz.
                if (len(approx) == 4):  # 4 Köşeli olup olmadığını kontrol edıyoruz.
                    IS_FOUND = 1
                    pts_src = np.array(approx, np.float32)

                    h, status = cv2.findHomography(pts_src, pts_dst)
                    out = cv2.warpPerspective(rgb, h, (int(_width + _margin * 2), int(_height + _margin * 2)))
                    cv2.drawContours(rgb, [approx], -1, (255, 0, 0), 2)
                else:
                    pass
            cv2.namedWindow('edges', cv2.WND_PROP_AUTOSIZE)
            cv2.imshow('edges', edges)

            cv2.namedWindow('rgb', cv2.WND_PROP_AUTOSIZE)
            cv2.imshow('rgb', rgb)
        if IS_FOUND:
            cv2.namedWindow('out', cv2.WND_PROP_AUTOSIZE)
            cv2.imshow('out', out)
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break
    time.sleep(DELAY)  # Belirlediğimiz delay değerine göre programı bekletiyoruz.

if USE_CAM : video_capture.release()
cv2.destroyAllWindows()







