import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QMessageBox, QAbstractItemView, QHeaderView, QTableWidgetItem

from src.core.adminsql import AdminSql
from src.core.leavesql import LeaveSql
from src.core.util import Util
from src.gui.admiwidget.admin.ui_leave import Ui_Leave


class LeaveWidget(QWidget, Ui_Leave):

    def __init__(self, parent=None):
        super(LeaveWidget, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        LeaveSql.sql_init()
        # LeaveSql.delete_table()
        LeaveSql.creat_table()
        # print(Util.get_leave_num())
        # LeaveSql.insert('2016117249', "申俊", "19点49分", "555", False)


    def _initWidget(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        header = ["学号", "姓名", "请假开始时间", "请假结束时间", "     是否同意     "]
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)

        self._clear()
        # self._append_to_table('2016117249', "申俊", "19点49分", "333", False)
        results = LeaveSql.select_all()
        print(results)
        if results is None:
            return
        for result in results:
            self._append_to_table(result[0], result[1], result[2], result[3], result[4])


    def _initConnect(self):
        self.tableWidget.cellChanged.connect(self._changed)

    def _changed(self, row, col):
        id = self.tableWidget.item(row, 0).text()
        startTime = self.tableWidget.item(row, 2).text()
        if self.tableWidget.item(row, col).checkState() == Qt.Checked:
            LeaveSql.update_agree_by_id_startTime(id, startTime, True)
        elif self.tableWidget.item(row, col).checkState() == Qt.Unchecked:
            LeaveSql.update_agree_by_id_startTime(id, startTime, False)

        results = LeaveSql.select_all()
        print(results)



    def _clear(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        header = ["学号", "姓名", "请假开始时间", "请假结束时间", "     是否同意     "]
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)

    def _append_to_table(self, id, name, start_time, end_time, agree):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        font = QFont()
        font.setPointSize(13)
        id_item = QTableWidgetItem(str(id))
        id_item.setTextAlignment(Qt.AlignCenter)
        id_item.setFont(font)
        name_item = QTableWidgetItem(name)
        name_item.setTextAlignment(Qt.AlignCenter)
        name_item.setFont(font)
        sign_time_item = QTableWidgetItem(start_time)
        sign_time_item.setTextAlignment(Qt.AlignCenter)
        sign_time_item.setFont(font)
        signOK_item = QTableWidgetItem(end_time)
        signOK_item.setTextAlignment(Qt.AlignCenter)
        signOK_item.setFont(font)

        agree_item = QTableWidgetItem("同意")
        agree_item.setFont(font)
        if agree:
            agree_item.setCheckState(Qt.Checked)
        else:
            agree_item.setCheckState(Qt.Unchecked)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, id_item)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, name_item)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, sign_time_item)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, signOK_item)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 4, agree_item)






