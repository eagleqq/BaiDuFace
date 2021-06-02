import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from cv2 import cv2
import time
from PIL import Image, ImageDraw, ImageFont

# 相机读取线程
from src.core.faceinterface import FaceInterface
from src.core.signsql2 import Sign2Sql


class CamReadThread(QThread):
    signalFrame = pyqtSignal(object)
    signalFailed = pyqtSignal(str)
    signalResult = pyqtSignal(str)  # id , image

    def __init__(self, parent=None):
        super(CamReadThread, self).__init__(parent)
        self.work = False
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

    # def getIsCanClock(self):
    #     Sign2Sql.sql_init()
    #     Sign2Sql.creat_table()
    #     Sign2Sql.select_all()

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
                # todo: 调用匹配算法
                rect = self.facesdk.detect(frame)
                for x, y, w, h in rect:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # 当只有一个人
                if len(rect) == 1:  # 当只有一个人时
                    self.count += 1
                    frame = self.drawText("请面向摄像头保持别动(5),{} ".format(self.count), frame)
                    print(self.count)
                    if self.count == 5:  # 保持5次
                        self.count = 0
                        x, y, w, h = rect[0]
                        face_roi = frame[(y - 2):y + h + 4, (x - 2):x + w + 4]
                        cv2.imwrite('./data/image/face.png', face_roi)
                        cv2.imwrite('./data/image/all.png', frame)
                        frame = self.drawText("正在匹配中...", frame, 50, 100)
                        self.signalFrame.emit(frame)
                        face_fd = open('./data/image/face.png', 'rb').read()
                        islive = self.facesdk.getIsLive(face_fd)
                        if islive:
                            score, user_id = self.facesdk.search(face_fd)
                            frame = self.drawText("学号：{}， 相似度：{}".format(user_id, score), frame, 50, 150)
                            self.signalResult.emit(user_id)
                        else:
                            frame = self.drawText("检测到人脸并非活体",  frame, 50, 150)
                else:
                    self.count = 0
                self.signalFrame.emit(frame)
            self.capture.release()
            print("释放")
        except Exception as err:
            self.signalFailed.emit(str(err))
