import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from src.gui.userwidget import ui_recordwidget

class RecordWidget(QWidget, ui_recordwidget.Ui_Form):
    def __init__(self):
        super(RecordWidget, self).__init__()
        self.setupUi(self)

    def setFace(self, face_image):
        """
        设置头像
        :param face_image:
        :return:
        """
        # 设置图像源 和 图像大小
        result_frame = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
        qtImg = QImage(result_frame.data,
                       result_frame.shape[1],
                       result_frame.shape[0],
                       QImage.Format_RGB888)
        self.label.setScaledContents(True)
        self.label.setPixmap(QPixmap.fromImage(qtImg))

    def setName(self, name):
        """
        设置姓名
        :param name:
        :return:
        """
        self.label_name.setText("姓名：" + name)

    def setSid(self, sid):
        """
        设置学号
        :param sid:
        :return:
        """
        self.label_sid.setText("学号：" +sid)

    def setDate(self, data):
        """
        设置日期
        :param data:
        :return:
        """
        self.label_data.setText("打卡日期：" + data)

    def setTime(self, time):
        """
        设置时间
        :param time:
        :return:
        """
        self.label_time.setText("打卡时间：" + time)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = RecordWidget()
    win.show()
    sys.exit(app.exec_())


