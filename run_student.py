from src.gui.publicwidget.loginwidget import LoginWidget, LoginType
from src.gui.studentwidget.studentmainwindow import StudentMainWindow

print("学生端界面程序入口")

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    student_win = StudentMainWindow()
    student_win.setWindowTitle("学生端")
    login = LoginWidget(LoginType.Student)  # 学生登陆
    login.exec_()
    print("---1")
    if login.getIsLogin():
        print("---2")
        username = login.getLoginUsername()
        print("登陆的用户名", username)
        student_win.setUsername(username)
        student_win.updateRecordTable()
        student_win.show()
    print("---3")
    sys.exit(app.exec_())
