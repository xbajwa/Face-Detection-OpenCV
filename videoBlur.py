import cv2
import os
import pathlib
from typing import List
import numpy as np
import pandas as pd
from face_recognition.api import face_detector

ann = pd.read_csv(f'C:/Users/DELL/Desktop/week 1-5/Visual Data/Project/annotations.txt', delimiter='\t', header=None)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

class VideoClass:
    def __init__(self, name, vid):
        self.name = name
        self.video = vid

    def videoShow(self):
        i = 0
        while self.video.isOpened():
            ret, frame = self.video.read()

            if ret:
                nf = self.video.get(cv2.CAP_PROP_POS_FRAMES)
                if nf > 2:
                    pic = int(nf) - 3
                    print('pic', pic)
                    if ann.values[i, 0] == pic:
                        while True:
                            if ann.values[i, 0] != pic:
                                break
                            column = round(ann.values[i, 1])
                            row = round(ann.values[i, 2])
                            width = round(ann.values[i, 3] - 15)
                            height = round(ann.values[i, 4] - 112)
                            i = i + 1
                            cv2.rectangle(frame, (column, row), (column + width, row + height), (0, 255, 255), 1)
                    cv2.imshow(self.name, frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                         break

videos: List[VideoClass] = []
folder = 'C:/Users/DELL/Desktop/week 1-5/Visual Data/VIRAT Ground Dataset/videos_original/'
entries = os.listdir('C:/Users/DELL/Desktop/week 1-5/Visual Data/VIRAT Ground Dataset/videos_original/')
for filename in entries:
    vid = cv2.VideoCapture(str(folder) + str(filename))
    if vid is not None:
        obj = VideoClass(filename, vid)
        videos.append(obj)
        print("Loading...")

print(len(videos))
VideoClass.videoShow(videos[5])
