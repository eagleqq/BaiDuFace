import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from cv2 import cv2
import time
from PIL import Image, ImageDraw, ImageFont

# 相机读取线程
from src.core.faceinterface import FaceInterface


class RegisterThread(QThread):
    signalFrame = pyqtSignal(object)
    signalFailed = pyqtSignal(str)
    signalResult = pyqtSignal(str)  # id , image

    def __init__(self, parent=None):
        super(RegisterThread, self).__init__(parent)
        self.work = False
        self.addFaceFlag = False
        self.facesdk = FaceInterface()

    def threadStart(self):
        self.start()

    def threadStop(self):
        self.work = False

    def drawText(self, text="", img="",  x=50, y=50):
        cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pilimg = Image.fromarray(cv2img)
        draw = ImageDraw.Draw(pilimg)
        font = ImageFont.truetype("./data/config/SimHei.ttf", 20, encoding="utf-8")
        draw.text((x, y), text, (255, 0, 0), font=font)
        cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
        return cv2charimg

    def run(self):
        try:
            self.work = True
            self.capture = cv2.VideoCapture(0)
            success, frame = self.capture.read()
            self.signalFrame.emit(frame)
            self.count = 0
            while True:
                if not self.work:
                    break
                time.sleep(0.1)
                success, frame = self.capture.read()
                if self.addFaceFlag:
                    rect = self.facesdk.detect(frame)
                    for x, y, w, h in rect:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    if len(rect) == 1:  # 当只有一个人时
                        self.count += 1
                        frame = self.drawText("请面向摄像头保持别动(5),{} ".format(self.count), frame)
                        print(self.count)
                        if self.count == 5:  # 保持5次
                            self.count = 0
                            x, y, w, h = rect[0]
                            face_roi = frame[(y - 2):y + h + 4, (x - 2):x + w + 4]
                            cv2.imwrite('./data/image/register_face.png', face_roi)
                            frame = self.drawText("已注册", frame, 50, 150)
                            self.signalFrame.emit(frame)
                            self.signalResult.emit("已注册")
                    else:
                        self.count = 0
                self.signalFrame.emit(frame)
            self.capture.release()
            print("释放")
        except Exception as err:
            self.signalFailed.emit(str(err))
