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
                            width = round(ann.values[i, 3] )#- 12) # - 12
                            height = round(ann.values[i, 4] )#- 112) # - 112
                            kernel_width = (width // 7) | 1
                            kernel_height = (height // 7) | 1
                            if column % 2 == 0:
                                column = column + 1
                            if row % 2 == 0:
                                row = row + 1
                            cv2.rectangle(frame, (column, row), (column + width - 12, row + height - 112), (0, 255, 255), 1)
                            face_color = frame[row:row + height, column:column + width]
                            #blur = cv2.medianBlur(face_color, 9)
                            #blur = cv2.bilateralFilter(face_color, 51, 75, 75)
                            #blur = cv2.GaussianBlur(face_color, (13,13),0)
                            blur = cv2.GaussianBlur(face_color, (kernel_width, kernel_height), 0)

                            frame[row:row + height, column:column + width] = blur
                            i = i + 1
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
