import cv2 as cv
import numpy as np
img = cv.imread('Images/1.jpg')

blank = np.zeros((500, 500, 3), dtype='uint8')


blank[:] = 0, 0, 0

cv.circle(blank, (blank.shape[1]//2,
                  blank.shape[0]//2), 40, (0, 0, 255), thickness=-3)

cv.imshow("Circle", blank)


# line


cv.line(blank, (0, 0), (blank.shape[1]//2,
                        blank.shape[0]//2), (255, 255, 255), thickness=3)


# Text

cv.imshow("Line", blank)


cv.putText(blank, 'Hello', (255, 255),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)

cv.imshow("Text", blank)
cv.waitKey(0)
