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

cv.imshow("Canny Edges", canny)


contoursm hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
cv.waitKey(0)
