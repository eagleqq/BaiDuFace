import os
from PyQt5.QtWidgets import QMainWindow

from src.gui.admiwidget.admin.classwidget import ClassWidget
from src.gui.admiwidget.admin.ui_admin import Ui_Admin


class AdminWindow(QMainWindow, Ui_Admin):

    def __init__(self, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        self.class_widget = ClassWidget()


    def _initWidget(self):
        self.tabWidget.insertTab(0, self.class_widget, "班级管理")


    def _initConnect(self):
        pass


