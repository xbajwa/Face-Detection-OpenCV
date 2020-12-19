
import cv2
import os
import pathlib
from typing import List
import numpy as np
import pandas as pd

directory = 'C:/Users/opera_user/PycharmProjects/FaceDet'
os.chdir(directory)


class VideoClass:
    def __init__(self, name, vid):
        self.name = name
        self.video = vid

    def videoShow(self,K):
        i = 0
        print(os.getcwd())
        while self.video.isOpened():
            ret, frame = self.video.read()
            if ret:
                nf = self.video.get(cv2.CAP_PROP_POS_FRAMES)
                if int(nf) == int(self.video.get(cv2.CAP_PROP_FRAME_COUNT)):
                    cv2.destroyAllWindows()
                    break
                if int(self.video.get(cv2.CAP_PROP_FRAME_COUNT)) > 5000:
                    if int(nf-1) % 1000 == 0:
                        name = str(K) + str("p") + str(int(nf) - 1) + str(".bmp")
                        cv2.imwrite(str(name), frame)
                        print(name)
                else:
                    if int(nf-1) % 100 == 0:
                        name = str(K) + str("p") + str(int(nf) - 1) + str(".bmp")
                        cv2.imwrite(str(name), frame)
                        print(name)
                #print(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

                cv2.imshow(self.name, frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
  

videos: List[VideoClass] = []

folder = 'C:/Users/opera_user/Downloads/rand/VIRAT Ground Dataset/videos_original/'
entries = os.listdir('C:/Users/opera_user/Downloads/rand/VIRAT Ground Dataset/videos_original/')
for filename in entries:
    vid = cv2.VideoCapture(str(folder) + str(filename))
    if vid is not None:
        obj = VideoClass(filename, vid)
        videos.append(obj)
        print("Loading...")



print(len(videos))
#print(videos[0].video)
for j in range(1,328,2):
    VideoClass.videoShow(videos[j],j)










