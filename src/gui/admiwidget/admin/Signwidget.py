import os

import cv2
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QIntValidator, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView, QHeaderView

from src.core.adminsql import AdminSql
from src.core.faceinterface import FaceInterface
from src.core.signsql2 import Sign2Sql
from src.core.studentsql import StudentSql
from src.gui.admiwidget.admin.ui_face import Ui_Face
from src.gui.admiwidget.admin.ui_sign import Ui_Sign
from src.gui.admiwidget.registerthread import RegisterThread


class SignWidget(QWidget, Ui_Sign):

    def __init__(self, parent=None):
        super(SignWidget, self).__init__(parent)
        self.setupUi(self)
        self.facesdk = FaceInterface()

        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        Sign2Sql.sql_init()
        Sign2Sql.creat_table()

    def _initWidget(self):
        self.dateTimeEdit.setDate(QDate.currentDate())
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(1)
        header = ["上课打卡时间"]
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self._clear()
        results = Sign2Sql.select_all()
        print(results)
        if results is None:
            return
        for result in results:
            self._append_to_table(result)

    def _initConnect(self):
        self.pushButton_add_student.clicked.connect(self._add)

    def _clear(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(1)
        header = ["上课打卡时间"]
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def _append_to_table(self, time):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        font = QFont()
        font.setPointSize(13)
        id_item = QTableWidgetItem(time)
        id_item.setTextAlignment(Qt.AlignCenter)
        id_item.setFont(font)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, id_item)

    def _add(self):
        date = self.dateTimeEdit.dateTime()
        print(date.date().toPyDate())
        print(date.time().toPyTime())
        time = str(date.date().toPyDate()) + " " + str(date.time().toPyTime())
        print(time)
        self._append_to_table(time)
        Sign2Sql.insert(time)
