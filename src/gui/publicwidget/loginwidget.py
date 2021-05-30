from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog

from src.core.adminsql import AdminSql
from src.core.constants import STUDENT_LOGIN_INFO_PATH, ADMIN_LOGIN_INFO_PATH
from src.core.logindata import LoginData
from src.core.studentsql import StudentSql
from src.gui.publicwidget import ui_login
from enum import Enum

# 登陆类型枚举
class LoginType(Enum):
    Student = 1
    Admin = 2

# 登陆窗口
class LoginWidget(QDialog, ui_login.Ui_Form):

    def __init__(self, login_type=LoginType.Student):
        super(LoginWidget, self).__init__()
        self.setupUi(self)
        self.isloginsuccess = False  # 是否登陆成功
        self.login_username = None  # 登陆的账号
        self.login_type = login_type
        self.pushButton_login.clicked.connect(self.slotLogin)
        self.pushButton_exit.clicked.connect(self.slotExit)
        if self.login_type == LoginType.Student:
            self.login_info_config = LoginData(STUDENT_LOGIN_INFO_PATH)
            StudentSql.sql_init()
        elif self.login_type == LoginType.Admin:
            self.login_info_config = LoginData(ADMIN_LOGIN_INFO_PATH)
            AdminSql.sql_init()
            AdminSql.creat_table()
            AdminSql.insert(0, "admin", "admin", "无")
        username, password = self.login_info_config.getInfo()
        self.lineEdit_username.setText(username)
        self.lineEdit_pwd.setText(password)

    def slotLogin(self):
        """
        登陆
        :return:
        """
        self.isloginsuccess = False
        username = self.lineEdit_username.text()
        password = self.lineEdit_pwd.text()
        if not username:
            QMessageBox.information(self, "提示", "账号输入为空!")
            return
        if not password:
            QMessageBox.information(self, "提示", "密码输入为空!")
            return
        if self.login_type == LoginType.Student:
            if username == password:  # 学生端用户名、密码一致
                student_dict = StudentSql.select_all_dict()
                print("所有学生信息", student_dict)
                if username in student_dict.keys(): # 在数据库中存在该学号
                    self.login_username = username
                    if self.checkBox_remember.isChecked():
                        self.login_info_config.setInfo(username, password)
                    self.isloginsuccess = True
                    QMessageBox.information(self, "成功", "登录成功")
                    self.close()
                else:
                    QMessageBox.warning(self, "错误", "账号或密码错误")
            else:
                QMessageBox.warning(self, "错误", "账号或密码错误")
        elif self.login_type == LoginType.Admin:
            admin = AdminSql.select_by_id(0)
            if admin[1] == username and admin[2] == password:
                self.login_username = username
                if self.checkBox_remember.isChecked():
                    self.login_info_config.setInfo(username, password)
                self.isloginsuccess = True
                QMessageBox.information(self, "成功", "登录成功")
                self.close()
            else:
                QMessageBox.warning(self, "错误", "账号或密码错误")

    def slotExit(self):
        self.close()

    def getIsLogin(self):
        """
        获取是否登陆成功
        :return:
        """
        return self.isloginsuccess

    def getLoginUsername(self):
        """
        获取登陆用户名
        :return:
        """
        return self.login_username

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = LoginWidget()
    win.show()
    sys.exit(app.exec_())
