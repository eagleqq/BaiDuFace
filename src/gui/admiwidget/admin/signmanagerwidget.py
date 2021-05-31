import csv
import os

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QTableWidgetItem, QFileDialog, QMessageBox

from src.core.signsql import SignSql

from src.gui.admiwidget.admin.ui_signmanager import Ui_SignManager


class SignManagerWidget(QWidget, Ui_SignManager):

    def __init__(self, parent=None):
        super(SignManagerWidget, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        SignSql.sql_init()
        SignSql.creat_table()

    def _initWidget(self):
        self.dateEdit.setDate(QDate.currentDate())
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        header = ["id", "姓名", "签到时间", "签到状态"]
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self._clear()
        results = SignSql.select_all()
        if results is None:
            return
        for result in results:
            if result[3]:
                self._append_to_table(result[0], result[1], result[2], "有效")
            else:
                self._append_to_table(result[0], result[1], result[2], "无效")

    def _initConnect(self):
        self.pushButton_select_id.clicked.connect(self._select_id)
        self.pushButton_select_time.clicked.connect(self._select_time)
        self.pushButton_clear.clicked.connect(self._clear2)
        self.pushButton_export.clicked.connect(self._export)

    def _select_id(self):
        self._clear()
        id = self.lineEdit_id.text()
        results = SignSql.select_by_id(id)
        if results is None:
            return
        for result in results:
            if result[3]:
                self._append_to_table(result[0], result[1], result[2], "有效")
            else:
                self._append_to_table(result[0], result[1], result[2], "无效")

    def _select_time(self):
        self._clear()
        date = self.dateEdit.date()
        if date.month() < 10:
            time = str(date.year()) + "-" + "0" + str(date.month())
        else:
            time = str(date.year()) + "-" + str(date.month())
        if date.day() < 10:
            time += "-" + "0" + str(date.day())
        else:
            time += "-" + str(date.day())
        print(time)
        results = SignSql.select_by_time(time)
        if results is None:
            return
        for result in results:
            if result[3]:
                self._append_to_table(result[0], result[1], result[2], "有效")
            else:
                self._append_to_table(result[0], result[1], result[2], "无效")

    def _export(self):
        if self.tableWidget.rowCount() == 0:
            QMessageBox.warning(self, "错误", "导出失败,数据为空")
            return
        path = QFileDialog.getExistingDirectory(self, "选择导出目录")
        if path == "":
            return
        with open(os.path.join(path, "export.csv"), 'w', encoding='utf8') as csvfile:
            fieldnames = ['学号', '姓名', '签到时间', '签到状态']
            writer = csv.writer(csvfile)
            # 注意header是个好东西
            # writer.writeheader()
            writer.writerow(fieldnames)
            for row in range(self.tableWidget.rowCount()):
                id = self.tableWidget.item(row, 0).text()
                name = self.tableWidget.item(row, 1).text()
                time = self.tableWidget.item(row, 2).text()
                ok = self.tableWidget.item(row, 3).text()
                writer.writerow((id, name, time, ok))
            QMessageBox.information(self, "成功", "导出成功")

    def _clear(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        header = ["id", "姓名", "签到时间", "签到状态"]
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def _clear2(self):
        self._clear()
        results = SignSql.select_all()
        if results is None:
            return
        for result in results:
            if result[3]:
                self._append_to_table(result[0], result[1], result[2], "有效")
            else:
                self._append_to_table(result[0], result[1], result[2], "无效")

    def _append_to_table(self, id, name, sign_time, signOK):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
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
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, id_item)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, name_item)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, sign_time_item)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, signOK_item)





