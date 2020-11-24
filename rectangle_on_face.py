import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')

# Selecting Haar-like features
# Creating an integral image
# Running AdaBoost training
# Creating classifier cascades

img = cv.imread('test.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Loading the classifier and creating a cascade object for face detection
faces = face_cascade.detectMultiScale(gray)

for (column, row, width, height) in faces:
    cv.rectangle(
        img,
        (column, row),
        (column + width, row + height),
        (0, 255, 0),
        2
    )

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()