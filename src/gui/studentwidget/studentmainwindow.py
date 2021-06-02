from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QAbstractItemView, QHeaderView

from src.core.leavesql import LeaveSql
from src.core.signsql import SignSql
from src.core.studentsql import StudentSql
from src.gui.studentwidget import ui_studentmainwindow


class StudentMainWindow(QMainWindow, ui_studentmainwindow.Ui_MainWindow):
    def __init__(self):
        super(StudentMainWindow, self).__init__()
        self.setupUi(self)
        self.__username = ""
        StudentSql.sql_init()
        StudentSql.creat_table()
        LeaveSql.sql_init()
        LeaveSql.creat_table()
        # print(Util.get_leave_num())

        self.stackedWidget.setCurrentWidget(self.page_leave)
        self.toolButton_leave.clicked.connect(self.slotCheckoutLeave)
        self.toolButton_record.clicked.connect(self.slotCheckoutRecord)
        self.pushButton_submit.clicked.connect(self.slotLeaveSubmit)
        self.pushButton_refresh.clicked.connect(self.updateRecordTable)

        self.dateTimeEdit_start.setDate(QDate.currentDate())
        self.dateTimeEdit_end.setDate(QDate.currentDate())
        self.groupBox_leave.setVisible(False)

    def setUsername(self, username):
        """
        设置用户名
        :param username:
        :return:
        """
        self.__username = username
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
        id = self.lineEdit_id.text()
        name = self.lineEdit_name.text()
        start_time = self.dateTimeEdit_start.text()
        end_time = self.dateTimeEdit_end.text()
        print(id, name, start_time, end_time)
        LeaveSql.insert(id, name, start_time, end_time, False)
        QMessageBox.information(self, "提示", "提交成功!")

    def updateRecordTable(self):
        """
        刷新打卡数据
        :return:
        """
        self.tableWidget_record.clear()
        self.initRecordTable()
        results = SignSql.select_all()
        if results is None:
            return
        for result in results:
            print(result[0], self.__username)
            if result[0] == self.__username:
                if result[3]:
                    self._append_to_record_table(result[0], result[1], result[2], "有效")
                else:
                    self._append_to_record_table(result[0], result[1], result[2], "无效")

    def initRecordTable(self):
        self.tableWidget_record.setRowCount(0)
        self.tableWidget_record.setColumnCount(4)
        header = ["学号", "姓名", "签到时间", "签到状态"]
        self.tableWidget_record.verticalHeader().setVisible(False)
        self.tableWidget_record.setHorizontalHeaderLabels(header)
        self.tableWidget_record.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_record.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_record.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def _append_to_record_table(self, id, name, sign_time, signOK):
        """
        表格中插入一行数据
        :param id:
        :param name:
        :param sign_time:
        :param signOK:
        :return:
        """
        self.tableWidget_record.setRowCount(self.tableWidget_record.rowCount() + 1)
        font = QFont()
        font.setPointSize(13)
        id_item = QTableWidgetItem(str(id))
        id_item.setTextAlignment(Qt.AlignCenter)
        id_item.setFont(font)
        name_item = QTableWidgetItem(name)
        name_item.setTextAlignment(Qt.AlignCenter)
        name_item.setFont(font)
        sign_time_item = QTableWidgetItem(sign_time)
        sign_time_item.setTextAlignment(Qt.AlignCenter)
        sign_time_item.setFont(font)
        signOK_item = QTableWidgetItem(signOK)
        signOK_item.setTextAlignment(Qt.AlignCenter)
        signOK_item.setFont(font)
        self.tableWidget_record.setItem(self.tableWidget_record.rowCount() - 1, 0, id_item)
        self.tableWidget_record.setItem(self.tableWidget_record.rowCount() - 1, 1, name_item)
        self.tableWidget_record.setItem(self.tableWidget_record.rowCount() - 1, 2, sign_time_item)
        self.tableWidget_record.setItem(self.tableWidget_record.rowCount() - 1, 3, signOK_item)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = StudentMainWindow()
    win.show()
    sys.exit(app.exec_())
