import pathlib
from typing import List

import cv2
import os
from PIL import Image

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

class VideoClass:
    def __init__(self, name, vid):
        self.name = name
        self.video = vid


class ImageClass:
    def __init__(self, name, img, width, height):
        self.name = name
        self.im = img
        self.width = width
        self.height = height

    def imshow(self):
        cv2.imshow(self.name, self.im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


images: List[ImageClass] = []

#folder = 'C:/Users/opera_user/Downloads/archive/lfw-deepfunneled/lfw-deepfunneled/'
#entries = os.listdir('C:/Users/opera_user/Downloads/archive/lfw-deepfunneled/lfw-deepfunneled/')

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
            images.append(obj)
            print("Loading...")


for i in range(len(images)):
    faces = face_cascade.detectMultiScale(cv2.cvtColor(images[i].im, cv2.COLOR_BGR2GRAY))
    for (column, row, width, height) in faces:
        cv2.rectangle( images[i].im, (column, row), (column + width, row + height), (0, 255, 0), 2)
    ImageClass.imshow(images[i])
