from src.gui.admiwidget.admin.adminwindow import AdminWindow
import sys
from PyQt5.QtWidgets import QApplication
from src.gui.publicwidget.loginwidget import LoginWidget, LoginType

print("后台管理程序入口")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_win = AdminWindow()
    login = LoginWidget(LoginType.Admin)  # 管理员登陆
    login.exec_()
    if login.getIsLogin():
        admin_win.setUp()
        admin_win.show()
    sys.exit(app.exec_())
