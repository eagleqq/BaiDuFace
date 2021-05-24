
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget

from src.core.adminsql import AdminSql
from src.gui.admiwidget.admin.adminwindow import AdminWindow
from src.gui.admiwidget.sign.signupwindow import SignUpWindow
from src.gui.admiwidget.sign.ui_signin import Ui_Sign


class SignWindow(QMainWindow, Ui_Sign):

    def __init__(self, parent=None):
        super(SignWindow, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        AdminSql.sql_init()
        AdminSql.creat_table()
        AdminSql.insert(0, "admin", "admin", "0")

    def _initWidget(self):
        self.setWindowTitle("登录")
        admin = AdminSql.select_by_id(0)
        if admin[4]:
            self.checkBox_name.setChecked(True)
            self.lineEdit_name.setText(admin[1])
        if admin[5]:
            self.checkBox_name.setChecked(True)
            self.checkBox_password.setChecked(True)
            self.lineEdit_name.setText(admin[1])
            self.lineEdit_password.setText(admin[2])

    def _initConnect(self):
        self.pushButton_exit.clicked.connect(self._exit)
        self.pushButton_signin.clicked.connect(self._sign_in)
        self.checkBox_password.stateChanged.connect(self._password)

    def _exit(self):
        self.close()

    def _sign_in(self):
        name = self.lineEdit_name.text()
        password = self.lineEdit_password.text()

        admin = AdminSql.select_by_id(0)
        if admin[1] == name and admin[2] == password:
            QMessageBox.information(self, "成功", "登录成功")
            self._name_changed()
            self._password_changed()

            self.admin_win = AdminWindow()
            screen = QDesktopWidget().screenGeometry()
            size = self.admin_win.geometry()
            self.admin_win.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
            self.admin_win.show()
            self.close()
        else:
            QMessageBox.information(self, "错误", "账号密码错误")

    def _name_changed(self):
        if self.checkBox_name.isChecked():
            AdminSql.set_saveName(True)
        else:
            AdminSql.set_saveName(False)

    def _password_changed(self):
        if self.checkBox_password.isChecked():
            AdminSql.set_saveName(True)
            AdminSql.set_savePassword(True)
        else:
            AdminSql.set_savePassword(False)

    def _password(self):
        if self.checkBox_password.isChecked():
            self.checkBox_name.setChecked(True)

    def closeEvent(self, QCloseEvent):
        if not self.checkBox_password.isChecked():
            AdminSql.set_savePassword(False)
        if not self.checkBox_name.isChecked():
            AdminSql.set_saveName(False)
        QCloseEvent.accept()
