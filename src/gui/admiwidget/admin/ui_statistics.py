# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_statistics.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Statistics(object):
    def setupUi(self, Statistics):
        Statistics.setObjectName("Statistics")
        Statistics.resize(786, 497)
        self.gridLayout_4 = QtWidgets.QGridLayout(Statistics)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 5, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Statistics)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.tableWidget_2 = QtWidgets.QTableWidget(Statistics)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_2, 1, 2, 1, 2)
        self.tableWidget_3 = QtWidgets.QTableWidget(Statistics)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_3, 1, 4, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Statistics)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 1, 1, 1)

        self.retranslateUi(Statistics)
        QtCore.QMetaObject.connectSlotsByName(Statistics)

    def retranslateUi(self, Statistics):
        _translate = QtCore.QCoreApplication.translate
        Statistics.setWindowTitle(_translate("Statistics", "Form"))
        self.label.setText(_translate("Statistics", "签到记录："))
        self.label_2.setText(_translate("Statistics", "迟到记录："))
        self.label_3.setText(_translate("Statistics", "请假记录："))
        self.label_4.setText(_translate("Statistics", "查询班级："))
        self.label_5.setText(_translate("Statistics", "查询课程："))
        self.label_6.setText(_translate("Statistics", "查询日期："))
        self.label_7.setText(_translate("Statistics", "邮箱地址："))
        self.pushButton.setText(_translate("Statistics", "查询"))
        self.pushButton_2.setText(_translate("Statistics", "刷新"))
        self.pushButton_4.setText(_translate("Statistics", "导出表格"))
        self.pushButton_3.setText(_translate("Statistics", "发送至邮箱"))
