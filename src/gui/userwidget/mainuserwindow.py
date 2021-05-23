from PyQt5.QtWidgets import QMainWindow
from src.gui.userwidget import ui_mainuserwindow

class MainUserWindow(QMainWindow, ui_mainuserwindow.Ui_MainWindow):
    def __init__(self):
        super(MainUserWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = MainUserWindow()
    win.show()
    sys.exit(app.exec_())
