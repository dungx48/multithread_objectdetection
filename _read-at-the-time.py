import cv2
import threading
import os
import numpy as np
import torch
from PIL import Image

class VideoReaderThread(threading.Thread):
    def __init__(self, video_path):
        super().__init__()
        self.video_path = video_path
        self.cap = cv2.VideoCapture(self.video_path)
        self.frame = None
        self.is_running = True

    def run(self):
        while self.is_running:
            ret, frame = self.cap.read()
            if ret:
                self.frame = frame
            else:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def stop(self):
        self.is_running = False
        self.cap.release()

if __name__ == '__main__':
    model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5s.pt')
    root = '/home/vdungx/Project/video'
    threads = []
    for video_path in os.listdir(root):
        video_path = os.path.join(root,video_path)
        thread = VideoReaderThread(video_path)
        threads.append(thread)
        thread.start()

    while True:
        frames = []
        for thread in threads:
            frame = thread.frame
            print(frame.shape)
            frames.append(frame)
            # postprocess = model(frame)
            # print(postprocess)
            # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                
        if len(frames) == len(os.listdir(root)):
            pass
        #     # cv2.imshow('name', frame)
            # frames = np.stack(frames)
            # print(frames)
        #     print(frames.shape)
        #     postprocess = model(frames)
        #     print(postprocess)
            # print('------------------------------------------------------------')
            # cv2.imshow('name', frame)
            # print(str(frames.shape) + ',' + str(i))

        if cv2.waitKey(1) == ord('q'):
            break

    for thread in threads:
        thread.stop()
    cv2.destroyAllWindows()
