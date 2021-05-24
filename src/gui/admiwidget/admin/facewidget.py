import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView, QHeaderView

from src.core.adminsql import AdminSql
from src.core.studentsql import StudentSql
from src.gui.admiwidget.admin.ui_face import Ui_Face


class FaceWidget(QWidget, Ui_Face):

    def __init__(self, parent=None):
        super(FaceWidget, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        StudentSql.sql_init()
        StudentSql.creat_table()

    def _initWidget(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        header = ["id", "姓名", "是否上传"]
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        student_list = StudentSql.select_all()
        for student in student_list:
            if student[2]:
                self._append_to_table(student[0], student[1], "已上传")
            else:
                self._append_to_table(student[0], student[1], "未上传")

    def _initConnect(self):
        self.pushButton_add_student.clicked.connect(self._add_student)
        self.pushButton_add_face.clicked.connect(self._add_face)

    def _add_student(self):
        id = self.lineEdit_id.text()
        name = self.lineEdit_name.text()
        if id == "" or name == "":
            QMessageBox.warning(self, "错误", "基本信息不能为空")
            return
        StudentSql.insert(id, name, False)
        self._append_to_table(id, name, "未上传")
        QMessageBox.information(self, "成功", "添加成功")
        self.lineEdit_name.setText("")
        self.lineEdit_id.setText("")

    def _append_to_table(self, id, name, has_upload):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        font = QFont()
        font.setPointSize(13)
        id_item = QTableWidgetItem(str(id))
        id_item.setTextAlignment(Qt.AlignCenter)
        id_item.setFont(font)
        name_item = QTableWidgetItem(name)
        name_item.setTextAlignment(Qt.AlignCenter)
        name_item.setFont(font)
        has_upload_item = QTableWidgetItem(has_upload)
        has_upload_item.setTextAlignment(Qt.AlignCenter)
        has_upload_item.setFont(font)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, id_item)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, name_item)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, has_upload_item)

    def _add_face(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            QMessageBox.warning(self, "错误", "未选中学生")
            return
        id = self.tableWidget.item(row, 0).text()
        # todo 上传

        StudentSql.update_uploadFace_by_id(id, True)
        self.tableWidget.item(row, 0).setText("已上传")



