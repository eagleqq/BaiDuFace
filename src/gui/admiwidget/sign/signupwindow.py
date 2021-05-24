import os

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from src.gui.admiwidget.sign.ui_signup import Ui_SignUp


class SignUpWindow(QMainWindow, Ui_SignUp):

    def __init__(self, parent=None):
        super(SignUpWindow, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        pass

    def _initWidget(self):
        self.setWindowTitle("注册")
        intValidator = QIntValidator()
        self.lineEdit_id.setValidator(intValidator)
        self.lineEdit_classId.setValidator(intValidator)

    def _initConnect(self):
        self.pushButton_signup.clicked.connect(self._sign_up)

    def _sign_up(self):
        id = self.lineEdit_id.text()
        password1 = self.lineEdit_password.text()
        password2 = self.lineEdit_password_2.text()
        name = self.lineEdit_name.text()
        eng_name = self.lineEdit_ename.text()
        class_id = self.lineEdit_classId.text()

        if len(id) < 1:
            QMessageBox.warning(self, "错误", "id不能为空")
            return
        if password1 != password2:
            QMessageBox.warning(self, "错误", "密码不一致")
            return
        result = UserSql.insert(id, password1, name, eng_name, class_id, False)
        if not result:
            QMessageBox.warning(self, "错误", "id重复，注册失败")
            return
        QMessageBox.information(self, "成功", "注册成功")
        self.close()

