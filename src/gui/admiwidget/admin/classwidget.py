import os
from PyQt5.QtWidgets import QWidget, QMessageBox

from src.gui.admiwidget.admin.ui_class import Ui_Class


class ClassWidget(QWidget, Ui_Class):

    def __init__(self, parent=None):
        super(ClassWidget, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        pass

    def _initWidget(self):
        self.pushButton_add.clicked.connect(self._add)

    def _initConnect(self):
        pass

    def _add(self):
        pass





