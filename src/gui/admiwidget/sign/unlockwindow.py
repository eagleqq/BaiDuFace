import os
from PyQt5.QtWidgets import QMainWindow
from project.gui.sign.ui_unlock import Ui_Unlock


class UnlockWindow(QMainWindow, Ui_Unlock):

    def __init__(self, parent=None):
        super(UnlockWindow, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        pass

    def _initWidget(self):
        pass

    def _initConnect(self):
        # self.pushButton_login.clicked.connect(self._login)
        self.pushButton_close.clicked.connect(self._close)

    # def _login(self):
    #     #  登录
    #     self.close()

    def _close(self):
        self.close()

