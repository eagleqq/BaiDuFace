# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_recordwidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(609, 146)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(self.groupBox)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.label_time = QtWidgets.QLabel(self.groupBox)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout.addWidget(self.label_time)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_sid = QtWidgets.QLabel(self.groupBox)
        self.label_sid.setObjectName("label_sid")
        self.horizontalLayout_2.addWidget(self.label_sid)
        self.label_data = QtWidgets.QLabel(self.groupBox)
        self.label_data.setObjectName("label_data")
        self.horizontalLayout_2.addWidget(self.label_data)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "头像"))
        self.label_name.setText(_translate("Form", "姓名"))
        self.label_time.setText(_translate("Form", "打卡时间"))
        self.label_sid.setText(_translate("Form", "学号"))
        self.label_data.setText(_translate("Form", "打卡日期"))

