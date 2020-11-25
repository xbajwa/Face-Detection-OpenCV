import pathlib
from typing import List

import cv2
import os

class VideoClass:
    def __init__(self, name, vid):
        self.name = name
        self.video = vid

    def videoShow(self):
        while self.video.isOpened():
            ret, frame = self.video.read()
            if ret:
                cv2.imshow(self.name, frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
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

# vid = cv2.VideoCapture('C:/Users/DELL/Desktop/week 1-5/Visual Data/VIRAT Ground Dataset/videos_original/VIRAT_S_000002.mp4')
#while vid.isOpened():
 #   ret, frame = vid.read()
  #  if ret:
   #     cv2.imshow('Frame', frame)
    #    if cv2.waitKey(25) & 0xFF == ord('q'):
     #       break
    #else:
     #   break
#vid.release()
#cv2.destroyAllWindows()