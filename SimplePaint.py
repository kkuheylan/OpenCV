import cv2 as cv
import numpy
import random

prev_x, prev_y = -1, -1
undo = []

def draw(event, x, y, flags, param):
    global prev_x, prev_y, contrast_factor, r, g, b, t

    if event == cv.EVENT_LBUTTONDOWN:
        prev_x, prev_y = x, y
        undo.append(img.copy())  # Save the current canvas as a backup

    elif event == cv.EVENT_MOUSEMOVE:
        if flags & cv.EVENT_FLAG_LBUTTON:
            r = cv.getTrackbarPos("RED", "paint")
            g = cv.getTrackbarPos("GREEN", "paint")
            b = cv.getTrackbarPos("BLUE", "paint")
            contrast_factor = cv.getTrackbarPos("CONTRAST", "paint") / 255.0
            t = cv.getTrackbarPos("THICKNESS", "paint")
            color = (int(b * contrast_factor), int(g * contrast_factor), int(r * contrast_factor))
            cv.line(img, (prev_x, prev_y), (x, y), color, t)
            prev_x, prev_y = x, y

    elif event == cv.EVENT_LBUTTONUP:
        prev_x, prev_y = -1, -1  # Reset the previous position when drawing stops

def rand():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    contrast = random.randint(0, 255)
    cv.setTrackbarPos("RED", "paint", r)
    cv.setTrackbarPos("GREEN", "paint", g)
    cv.setTrackbarPos("BLUE", "paint", b)
    cv.setTrackbarPos("CONTRAST", "paint", contrast)

img = numpy.ones((720, 1080, 3), numpy.uint8) * 255  # Create a white canvas
cv.namedWindow("paint", cv.WINDOW_NORMAL)
cv.setMouseCallback("paint", draw)

cv.createTrackbar("RED", "paint", 0, 255, lambda x: None)
cv.createTrackbar("GREEN", "paint", 0, 255, lambda x: None)
cv.createTrackbar("BLUE", "paint", 0, 255, lambda x: None)
cv.createTrackbar("CONTRAST", "paint", 0, 255, lambda x: None)
cv.createTrackbar("THICKNESS", "paint", 1, 100, lambda x: None)

while True:
    cv.imshow("paint", img)
    key = cv.waitKey(1) & 0xFF

    if key == ord('q') or key == ord('Q') or cv.getWindowProperty("paint", cv.WND_PROP_VISIBLE) < 1:
        break
    elif key == ord('r') or key == ord('R'):
        rand()
        print("Random")
    elif key == ord('c') or key == ord('C'):
        img = numpy.ones((720, 1080, 3), numpy.uint8) * 255
        print("Cleaned")
    elif key == ord('u') or key == ord('U') or key == 26:  # key == 26 = ctrl + z
        if len(undo) > 0:
            img = undo.pop()  # Restore the last saved canvas state
            print("Undo")
        else:
            print("Nothing")

cv.destroyAllWindows()
print("Finished")
