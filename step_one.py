import pathlib
from typing import List

import cv2
import os

from cv2.cv2 import imshow

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
class VideoClass:
    def __init__(self, name, vid):
        self.name = name
        self.video = vid

    def videoShow(self):
        while self.video.isOpened():
            ret, frame = self.video.read()
            if ret:
                faces = face_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
                for (column, row, width, height) in faces:
                    cv2.rectangle(frame, (column, row), (column + width, row + height), (0, 255, 0), 2)
                cv2.imshow(self.name, frame)
                key = cv2.waitKey(0)
                while key not in [ord('q'), ord('k')]:
                    key = cv2.waitKey(0)
                if key == ord('q'):
                    break
        self.video.release()
        cv2.destroyAllWindows()


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
print(videos[0].video)
VideoClass.videoShow(videos[0])

