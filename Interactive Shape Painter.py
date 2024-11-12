import cv2 as cv
import numpy
from math import sqrt

pre_x, pre_y = -1, -1

def draw(event, x, y, flags, param):
    global pre_x, pre_y
    if event == cv.EVENT_LBUTTONDOWN or event == cv.EVENT_RBUTTONDOWN:
        pre_x, pre_y = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if flags & cv.EVENT_FLAG_LBUTTON:
            radius = int(sqrt((x - pre_x) ** 2 + (y - pre_y) ** 2))
            cv.circle(img, (pre_x, pre_y), radius, (255, 192, 203), 10)
        elif flags & cv.EVENT_FLAG_RBUTTON:
            cv.rectangle(img, (pre_x, pre_y), (x, y), (203, 192, 255), 10)
    elif event == cv.EVENT_LBUTTONUP or event == cv.EVENT_RBUTTONUP:
        pre_x, pre_y = -1, -1

img = numpy.ones((720, 1080, 3), numpy.uint8) * 255
cv.namedWindow("paint", cv.WINDOW_NORMAL)
cv.setMouseCallback("paint", draw)

while True:
    cv.imshow("paint", img)
    if cv.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
        break
    elif cv.getWindowProperty("paint", cv.WND_PROP_VISIBLE) < 1:
        break

cv.destroyAllWindows()