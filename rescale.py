import cv2 as cv
img = cv.imread('Images/1.jpg')
cv.imshow('Image', img)


def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('Videos/kitten.mp4')

resized_image = rescaleFrame(img)
cv.imshow("Resized Image", resized_image)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
