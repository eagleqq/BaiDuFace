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
        self.pushButton_save.clicked.connect(self._save)
        admin = AdminSql.select_by_id(0)
        self.lineEdit_name.setText(admin[1])
        self.lineEdit_password.setText(admin[2])
        self.lineEdit_class.setText(admin[3])

    def _initConnect(self):
        pass

    def _save(self):
        name = self.lineEdit_name.text()
        password = self.lineEdit_password.text()
        className = self.lineEdit_class.text()
        if name == "" or password == "" or className == "":
            QMessageBox.warning(self, "错误", "基本信息不能为空")
            return
        AdminSql.update(name, password, className)
        QMessageBox.information(self, "成功", "修改成功")





