import os
from PyQt5.QtWidgets import QWidget, QMessageBox

from src.core.studentsql import StudentSql
from src.gui.admiwidget.admin.ui_signmanager import Ui_SignManager


class SignManagerWidget(QWidget, Ui_SignManager):

    def __init__(self, parent=None):
        super(SignManagerWidget, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        StudentSql.sql_init()
        StudentSql.creat_table()

    def _initWidget(self):
        pass

    def _initConnect(self):
        self.pushButton_select_id.clicked.connect(self._select_id)

    def _select_id(self):
        pass






