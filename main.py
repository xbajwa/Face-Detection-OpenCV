# importing OpenCV(cv2) module
import os
from typing import List

import cv2
import face_recognition
from PIL import Image


# img = cv2.imread('C:/Users/DELL/Desktop/week 1-5/Visual Data/Project/Data set/V&J/__MACOSX/lfw-deepfunneledAaron_Eckhart/._Aaron_Eckhart_0001.jpg')
# Output img with window name as 'image'
# cv2.imshow('image', img)
# Maintain output window utill
# user presses a key
# cv2.waitKey(0)
# Destroying present windows on screen
# cv2.destroyAllWindows()


class ImageClass:
    def __init__(self, name, img, width, height):
        self.name = name
        self.im = img
        self.width = width
        self.height = height
        self.scaleFactor = 1.3
        self.minNeighbors = 4
        self.minSize = 30
        self.maxSize = 30
        self.flags = cv2.CASCADE_SCALE_IMAGE

    def imshow(self):
        cv2.imshow(self.name, self.im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


images: List[ImageClass] = []

folder = 'C:/Users/DELL/Desktop/week 1-5/Visual Data/Project/Data set/V&J/lfw-deepfunneled/'
entries = os.listdir('C:/Users/DELL/Desktop/week 1-5/Visual Data/Project/Data set/V&J/lfw-deepfunneled/')
for entry in entries:
    name = str(folder) + str(entry)
    for filename in os.listdir(name):
        img = cv2.imread(str(name) + "/" + str(filename))
        im = Image.open(str(name) + "/" + str(filename))
        if img is not None:
            width, height = im.size
            obj = ImageClass(filename, img, width, height)
            obj.imshow(obj)
            images.append(obj)


print(len(images))
