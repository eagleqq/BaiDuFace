# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_leave.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Leave(object):
    def setupUi(self, Leave):
        Leave.setObjectName("Leave")
        Leave.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Leave)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Leave)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(Leave)
        QtCore.QMetaObject.connectSlotsByName(Leave)

    def retranslateUi(self, Leave):
        _translate = QtCore.QCoreApplication.translate
        Leave.setWindowTitle(_translate("Leave", "Form"))