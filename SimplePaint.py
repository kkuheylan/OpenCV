import cv2 as cv
import numpy as np
import random

prev_x, prev_y = -1, -1
temp_draw = []
temp_pen = [[0, 0, 0, 1, 1]]

def draw(event, x, y, flags, param):
    global prev_x, prev_y, r, g, b, t, contrast_factor

    if event == cv.EVENT_LBUTTONDOWN:
        prev_x, prev_y = x, y
        if len(temp_draw) == 0 or (len(temp_draw) > 0 and not np.array_equal(temp_draw[-1], img)):
            temp_draw.append(img.copy())

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
        prev_x, prev_y = -1, -1
        temp_draw.append(img.copy())

def rand():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    contrast = random.randint(0, 255)
    thickness = random.randint(1, 100)
    cv.setTrackbarPos("RED", "paint", r)
    cv.setTrackbarPos("GREEN", "paint", g)
    cv.setTrackbarPos("BLUE", "paint", b)
    cv.setTrackbarPos("CONTRAST", "paint", contrast)
    cv.setTrackbarPos("THICKNESS", "paint", thickness)
    print(f"Random Pen Set: R={r}, G={g}, B={b}, Contrast={contrast}, Thickness={thickness}")

def pen_undo():
    if len(temp_pen) > 1:
        temp_pen.pop()
        last_pen = temp_pen[-1]
        cv.setTrackbarPos("RED", "paint", last_pen[0])
        cv.setTrackbarPos("GREEN", "paint", last_pen[1])
        cv.setTrackbarPos("BLUE", "paint", last_pen[2])
        cv.setTrackbarPos("CONTRAST", "paint", last_pen[3])
        cv.setTrackbarPos("THICKNESS", "paint", last_pen[4])
    else:
        print("No More Pen Undo Steps")

img = np.ones((720, 1080, 3), np.uint8) * 255
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
    res_r = cv.getTrackbarPos("RED", "paint")
    res_g = cv.getTrackbarPos("GREEN", "paint")
    res_b = cv.getTrackbarPos("BLUE", "paint")
    res_contrast = cv.getTrackbarPos("CONTRAST", "paint")
    res_t = cv.getTrackbarPos("THICKNESS", "paint")

    if temp_pen[-1] != [res_r, res_g, res_b, res_contrast, res_t]:
        temp_pen.append([res_r, res_g, res_b, res_contrast, res_t])

    if key == ord('q'):
        break
    elif key == ord('r'):
        rand()
    elif key == ord('c'):
        img = np.ones((720, 1080, 3), np.uint8) * 255
        print("Canvas Cleared")
    elif key == ord('u') or key == 26:
        if len(temp_draw) > 0:
            img = temp_draw.pop()
            print("Undo Last Draw")
        else:
            print("No More Undo Steps")
    elif key == ord('p') or key == "P":
        pen_undo()
    elif key == "d" or key == "D":
        cv.setTrackbarPos("RED", "paint", 0)
        cv.setTrackbarPos("GREEN", "paint", 0)
        cv.setTrackbarPos("BLUE", "paint", 0)
        cv.setTrackbarPos("CONTRAST", "paint", 0)
        cv.setTrackbarPos("THICKNESS", "paint", 1)
        print("Pen Default Settings")

cv.destroyAllWindows()
print("Finished")

# Time Complexity: O(N)
# Space Complexity: O(N)
# Serhat Kayır
