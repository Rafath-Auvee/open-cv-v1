import cv2 as cv
import numpy as np


img = cv.imread('Images/1.jpg')
# cv.imshow("Image", img)

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow("Blank", blank)


# Painting the images a certain colour

blank[:] = 0, 0, 0

# Rectangle

cv.rectangle(blank, (0, 0), (215, 110), (0, 255, 0), thickness=-2)


cv.imshow("Rectangle", blank)

# cv.imshow("Green", blank)
cv.waitKey(0)
