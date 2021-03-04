import cv2 as cv
img2 = cv.imread("Images/1.jpg")


def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


img = rescaleFrame(img2)
# cv.imshow("Original Image", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)
# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow("Dilated", dilated)
# eroded
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("Eroded", eroded)
cv.waitKey(0)
