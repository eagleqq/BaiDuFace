import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from cv2 import cv2
import time
from PIL import Image, ImageDraw, ImageFont

# 相机读取线程
class CamReadThread(QThread):
    signalFrame = pyqtSignal(object)
    signalFailed = pyqtSignal(str)

    def __init__(self, parent=None):
        super(CamReadThread, self).__init__(parent)
        self.work = False

    def threadStart(self):
        self.start()

    def threadStop(self):
        self.work = False

    def drawText(self, text, img):
        cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pilimg = Image.fromarray(cv2img)
        draw = ImageDraw.Draw(pilimg)
        font = ImageFont.truetype("./data/config/SimHei.ttf", 20, encoding="utf-8")
        draw.text((50, 50), text, (255, 0, 0), font=font)
        cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
        return cv2charimg

    def run(self):
        try:
            self.work = True
            self.capture = cv2.VideoCapture(0)
            success, frame = self.capture.read()
            self.signalFrame.emit(frame)
            while True:
                if not self.work:
                    break
                time.sleep(0.01)
                success, frame = self.capture.read()
                frame = self.drawText("检测到人脸，正在匹配中...", frame)
                # todo: 调用匹配算法
                # print(success)
                self.signalFrame.emit(frame)
            self.capture.release()
            print("释放")
        except Exception as err:
            self.signalFailed.emit(str(err))
