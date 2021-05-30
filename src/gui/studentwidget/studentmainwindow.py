from PyQt5.QtWidgets import QMainWindow, QMessageBox

from src.core.studentsql import StudentSql
from src.gui.studentwidget import ui_studentmainwindow


class StudentMainWindow(QMainWindow, ui_studentmainwindow.Ui_MainWindow):
    def __init__(self):
        super(StudentMainWindow, self).__init__()
        self.setupUi(self)
        StudentSql.sql_init()
        self.stackedWidget.setCurrentWidget(self.page_leave)
        self.toolButton_leave.clicked.connect(self.slotCheckoutLeave)
        self.toolButton_record.clicked.connect(self.slotCheckoutRecord)
        self.pushButton_submit.clicked.connect(self.slotLeaveSubmit)

    def setUsername(self, username):
        """
        设置用户名
        :param username:
        :return:
        """
        self.lineEdit_id.setText(username)
        student_dict = StudentSql.select_all_dict()
        name = student_dict[username][0]
        self.lineEdit_name.setText(name)

    def slotCheckoutLeave(self):
        """
        切换到申请界面
        :return:
        """
        print("切换到申请界面")
        self.stackedWidget.setCurrentWidget(self.page_leave)

    def slotCheckoutRecord(self):
        """
        切换到考勤记录
        :return:
        """
        print("切换到考勤记录")
        self.stackedWidget.setCurrentWidget(self.page_record)

    def slotLeaveSubmit(self):
        """
        请假申请
        :return:
        """
        # 数据库
        QMessageBox.information(self, "提示", "提交成功!")


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = StudentMainWindow()
    win.show()
    sys.exit(app.exec_())
