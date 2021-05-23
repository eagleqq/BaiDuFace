from src.gui.userwidget.mainuserwindow import MainUserWindow

print("打卡界面程序入口")

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = MainUserWindow()
    win.setWindowTitle("百度人脸识别打卡")
    win.show()
    sys.exit(app.exec_())
