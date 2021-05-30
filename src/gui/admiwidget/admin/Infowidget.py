import os
from PyQt5.QtWidgets import QWidget, QMessageBox

from src.core.adminsql import AdminSql
from src.gui.admiwidget.admin.ui_info import Ui_Info


class InfoWidget(QWidget, Ui_Info):

    def __init__(self, parent=None):
        super(InfoWidget, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        AdminSql.sql_init()

    def _initWidget(self):
        admin = AdminSql.select_by_id(0)
        self.lineEdit_name.setText(admin[1])
        self.lineEdit_password.setText(admin[2])

    def _initConnect(self):
        self.pushButton_save.clicked.connect(self._save)

    def _save(self):
        name = self.lineEdit_name.text()
        password = self.lineEdit_password.text()
        print(name, password,)
        if name == "" or password == "":
            QMessageBox.warning(self, "错误", "基本信息不能为空")
            return
        result = AdminSql.update(name, password, "")
        print(result)
        admin = AdminSql.select_by_id(0)
        print(admin)
        QMessageBox.information(self, "成功", "修改成功")





