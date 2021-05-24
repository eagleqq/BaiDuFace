# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_info.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Info(object):
    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.resize(662, 593)
        self.gridLayout_2 = QtWidgets.QGridLayout(Info)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(Info)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout_2.addWidget(self.pushButton_save, 1, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(Info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.lineEdit_class = QtWidgets.QLineEdit(Info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_class.setFont(font)
        self.lineEdit_class.setObjectName("lineEdit_class")
        self.gridLayout.addWidget(self.lineEdit_class, 2, 1, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(Info)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Form"))
        self.pushButton_save.setText(_translate("Info", "修改设置"))
        self.label_3.setText(_translate("Info", "所带班级："))
        self.label_2.setText(_translate("Info", "密码："))
        self.label.setText(_translate("Info", "账号："))

