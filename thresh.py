import cv2 as cv
import cv2 as cv

img2 = cv.imread("Images/1.jpg")


def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


img = rescaleFrame(img2)

cv.imshow('Image', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Gray", gray)

canny = cv.Canny(img, 125, 175)

# cv.imshow("Canny Edges", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)


cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)
