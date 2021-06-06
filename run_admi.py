from src.core.adminsql import AdminSql
from src.core.leavesql import LeaveSql
from src.core.signsql import SignSql
from src.core.signsql2 import Sign2Sql
from src.core.studentsql import StudentSql
from src.gui.admiwidget.admin.adminwindow import AdminWindow
import sys
from PyQt5.QtWidgets import QApplication
from src.gui.publicwidget.loginwidget import LoginWidget, LoginType

print("后台管理程序入口")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    StudentSql.sql_init()
    StudentSql.creat_table()
    AdminSql.sql_init()
    AdminSql.creat_table()
    AdminSql.insert(0, "admin", "admin", "无")
    LeaveSql.sql_init()
    LeaveSql.creat_table()
    SignSql.sql_init()
    SignSql.creat_table()
    Sign2Sql.sql_init()
    Sign2Sql.creat_table()
    admin_win = AdminWindow()
    login = LoginWidget(LoginType.Admin)  # 管理员登陆
    login.exec_()
    if login.getIsLogin():
        admin_win.setUp()
        admin_win.show()
    sys.exit(app.exec_())
