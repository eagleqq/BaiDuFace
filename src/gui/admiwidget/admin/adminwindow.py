import os
from PyQt5.QtWidgets import QMainWindow

from src.gui.admiwidget.admin.Infowidget import InfoWidget
from src.gui.admiwidget.admin.facewidget import FaceWidget
from src.gui.admiwidget.admin.signmanagerwidget import SignManagerWidget
from src.gui.admiwidget.admin.ui_admin import Ui_Admin


class AdminWindow(QMainWindow, Ui_Admin):

    def __init__(self, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        self.info_widget = InfoWidget()
        self.face_widget = FaceWidget()
        self.sign_manager_widget = SignManagerWidget()

    def _initWidget(self):
        self.tabWidget.insertTab(0, self.info_widget, "个人信息")
        self.tabWidget.insertTab(1, self.face_widget, "人脸信息")
        self.tabWidget.insertTab(2, self.sign_manager_widget, "签到情况")

    def _initConnect(self):
        pass


