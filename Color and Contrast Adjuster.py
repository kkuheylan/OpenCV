import cv2 as cv
import numpy as np
import random


def colors_and_contrast(*cake):
    if cake: # If the user adjusts the settings manually
        r = cv.getTrackbarPos("R", "paint")
        g = cv.getTrackbarPos("G", "paint")
        b = cv.getTrackbarPos("B", "paint")
        d = cv.getTrackbarPos("D", "paint")
    else: # If the 'R' key is pressed
        """
        It could also be done using a button.
        """
        # Generate random values
        r = random.uniform(0, 255)
        g = random.uniform(0, 255)
        b = random.uniform(0, 255)
        d = random.uniform(0, 255)
        # Set the generated values to the trackbars
        cv.setTrackbarPos("R", "paint", int(r))
        cv.setTrackbarPos("G", "paint", int(g))
        cv.setTrackbarPos("B", "paint", int(b))
        cv.setTrackbarPos("D", "paint", int(d))

    k = d / 255.0 # Contrast factor
    # new_contrast = contrast * contrast multiplier
    # 255 is to make the appearance dark as the contrast approaches zero
    # If we don't, it's the opposite
    img[:] = np.clip([b * k, g * k, r * k, 255], 0, 255)


img = np.ones((720, 1080, 4), np.uint8) * 255
cv.namedWindow("paint", cv.WINDOW_AUTOSIZE)
cv.setMouseCallback("paint", colors_and_contrast)

cv.createTrackbar("R", "paint", 0, 255, colors_and_contrast)
cv.createTrackbar("G", "paint", 0, 255, colors_and_contrast)
cv.createTrackbar("B", "paint", 0, 255, colors_and_contrast)
cv.createTrackbar("D", "paint", 0, 255, colors_and_contrast)
# Trackbars creation
while True:
    cv.imshow("paint", img)

    key = cv.waitKey(1) & 0xFF
    if key == ord('r') or key == ord('R'):
        colors_and_contrast() # If 'R' key is pressed, we pass an empty value.

    if key in [ord('q'), ord('Q')] or cv.getWindowProperty("paint", cv.WND_PROP_VISIBLE) < 1:
        break

cv.destroyAllWindows()
s