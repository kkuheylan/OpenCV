import cv2 as cv
import numpy

pre_x, pre_y = -1, -1

def draw(event, x, y, flags, param):
    global pre_x, pre_y  # Make variables global
    if event == cv.EVENT_LBUTTONDOWN or event == cv.EVENT_RBUTTONDOWN:
        pre_x, pre_y = x, y  # Capture coordinates when left or right mouse button is pressed

    elif event == cv.EVENT_MOUSEMOVE:
        if flags & cv.EVENT_FLAG_SHIFTKEY and flags & cv.EVENT_FLAG_LBUTTON:  # Draw with white color (like an eraser) when Shift key and left button are pressed
            cv.line(img, (pre_x, pre_y), (x, y), (255, 255, 255), 10)
            pre_x, pre_y = x, y
        elif flags & cv.EVENT_FLAG_LBUTTON:  # Draw with purple color when left mouse button is pressed
            cv.line(img, (pre_x, pre_y), (x, y), (255, 192, 203), 10)
            pre_x, pre_y = x, y
        elif flags & cv.EVENT_FLAG_RBUTTON:  # Draw with pink color when right mouse button is pressed
            cv.line(img, (pre_x, pre_y), (x, y), (203, 192, 255), 10)
            pre_x, pre_y = x, y
    
    elif event == cv.EVENT_LBUTTONUP or event == cv.EVENT_RBUTTONUP:  # Reset coordinates when action is finished
        pre_x, pre_y = -1, -1

# Create a white canvas
img = numpy.ones((720, 1080, 3), numpy.uint8) * 255
cv.namedWindow("paint", cv.WINDOW_NORMAL)
cv.setMouseCallback("paint", draw)  # Set mouse callback to capture mouse events

while True:
    cv.imshow("paint", img)
    if cv.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:  # Exit if 'q' or 'Q' is pressed
        break
    elif cv.getWindowProperty("paint", cv.WND_PROP_VISIBLE) < 1:  # Exit if window is closed
        break

cv.destroyAllWindows()
