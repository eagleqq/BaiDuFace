from src.gui.admiwidget.sign.signwindow import SignWindow
import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget

print("后台管理程序入口")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = SignWindow()
    screen = QDesktopWidget().screenGeometry()
    size = mainwin.geometry()
    mainwin.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
    mainwin.show()
    sys.exit(app.exec_())