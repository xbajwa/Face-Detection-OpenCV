import cv2
import os
from typing import List


face_cascade = cv2.CascadeClassifier('C:/Users/opera_user/Downloads/rand/OpenCV DONT DELETE/x64/vc16/bin/cascade.xml')

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
                    cv2.rectangle(frame,(column, row),(column + width, row + height),(0, 255, 0),2)
                cv2.imshow(self.name, frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


videos: List[VideoClass] = []

folder = 'C:/Users/opera_user/Downloads/rand/VIRAT Ground Dataset/videos_original/'
entries = os.listdir('C:/Users/opera_user/Downloads/rand/VIRAT Ground Dataset/videos_original/')
entries = sorted(entries, key=len)
for filename in entries:
    vid = cv2.VideoCapture(str(folder) + str(filename))
    if vid is not None:
        obj = VideoClass(filename, vid)
        videos.append(obj)
        print("Loading...")

print(len(videos))
VideoClass.videoShow(videos[36])
