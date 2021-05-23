import datetime

import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow
from src.gui.userwidget import ui_mainuserwindow
from src.gui.userwidget.camreadthread import CamReadThread


class MainUserWindow(QMainWindow, ui_mainuserwindow.Ui_MainWindow):
    def __init__(self):
        super(MainUserWindow, self).__init__()
        self.setupUi(self)
        self.showTimeToLabel()
        # 摄像头读取线程
        self.cameraReadThread = CamReadThread()
        self.cameraReadThread.signalFrame.connect(self.slotUpdateImage)
        self.cameraReadThread.threadStart()

    def slotUpdateImage(self, frame):
        self.showImgToLabel(frame)
        self.showTimeToLabel()


    def showImgToLabel(self, frame):
        """
        显示图片到qt label上
        :param frame:  图片
        :return:
        """
        result_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        qtImg = QImage(result_frame.data,
                       result_frame.shape[1],
                       result_frame.shape[0],
                       QImage.Format_RGB888)
        self.label_img.setScaledContents(True)
        self.label_img.setPixmap(QPixmap.fromImage(qtImg))

    def showTimeToLabel(self):
        curr_time = datetime.datetime.now()
        data_str = "【" + datetime.datetime.strftime(curr_time, '%Y-%m-%d') + "】"
        time_str = datetime.datetime.strftime(curr_time, '%H:%M:%S')
        print(data_str + time_str)
        self.label_time.setText(data_str + time_str)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = MainUserWindow()
    win.show()
    sys.exit(app.exec_())
