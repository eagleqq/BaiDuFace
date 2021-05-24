# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_face.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Face(object):
    def setupUi(self, Face):
        Face.setObjectName("Face")
        Face.resize(813, 553)
        self.gridLayout = QtWidgets.QGridLayout(Face)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Face)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_id = QtWidgets.QLineEdit(Face)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.horizontalLayout.addWidget(self.lineEdit_id)
        self.label_2 = QtWidgets.QLabel(Face)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_name = QtWidgets.QLineEdit(Face)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.pushButton_add_student = QtWidgets.QPushButton(Face)
        self.pushButton_add_student.setObjectName("pushButton_add_student")
        self.horizontalLayout.addWidget(self.pushButton_add_student)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Face)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.tableWidget = QtWidgets.QTableWidget(Face)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_pic = QtWidgets.QLabel(Face)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pic.sizePolicy().hasHeightForWidth())
        self.label_pic.setSizePolicy(sizePolicy)
        self.label_pic.setObjectName("label_pic")
        self.verticalLayout.addWidget(self.label_pic)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_add_face = QtWidgets.QPushButton(Face)
        self.pushButton_add_face.setObjectName("pushButton_add_face")
        self.horizontalLayout_2.addWidget(self.pushButton_add_face)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.retranslateUi(Face)
        QtCore.QMetaObject.connectSlotsByName(Face)

    def retranslateUi(self, Face):
        _translate = QtCore.QCoreApplication.translate
        Face.setWindowTitle(_translate("Face", "Form"))
        self.label.setText(_translate("Face", "学号："))
        self.label_2.setText(_translate("Face", "姓名："))
        self.pushButton_add_student.setText(_translate("Face", "添加"))
        self.label_3.setText(_translate("Face", "学生列表："))
        self.label_pic.setText(_translate("Face", "pic"))
        self.pushButton_add_face.setText(_translate("Face", "添加人脸"))

