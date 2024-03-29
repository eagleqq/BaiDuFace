# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sign.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sign(object):
    def setupUi(self, Sign):
        Sign.setObjectName("Sign")
        Sign.resize(846, 584)
        Sign.setStyleSheet("font: 16pt \"新宋体\";")
        self.gridLayout = QtWidgets.QGridLayout(Sign)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Sign)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Sign)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout.addWidget(self.dateTimeEdit)
        self.pushButton_add_student = QtWidgets.QPushButton(Sign)
        self.pushButton_add_student.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_add_student.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_add_student.setObjectName("pushButton_add_student")
        self.horizontalLayout.addWidget(self.pushButton_add_student)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Sign)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.tableWidget = QtWidgets.QTableWidget(Sign)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.retranslateUi(Sign)
        QtCore.QMetaObject.connectSlotsByName(Sign)

    def retranslateUi(self, Sign):
        _translate = QtCore.QCoreApplication.translate
        Sign.setWindowTitle(_translate("Sign", "Form"))
        self.label.setText(_translate("Sign", "打卡时间："))
        self.pushButton_add_student.setText(_translate("Sign", "添加"))
        self.label_3.setText(_translate("Sign", "上课打卡时间："))
