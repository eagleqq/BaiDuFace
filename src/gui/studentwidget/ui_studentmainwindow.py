# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_studentmainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 733)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.toolButton_leave = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_leave.setMinimumSize(QtCore.QSize(100, 50))
        self.toolButton_leave.setObjectName("toolButton_leave")
        self.verticalLayout.addWidget(self.toolButton_leave)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.toolButton_record = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_record.setMinimumSize(QtCore.QSize(100, 50))
        self.toolButton_record.setObjectName("toolButton_record")
        self.verticalLayout.addWidget(self.toolButton_record)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_leave = QtWidgets.QWidget()
        self.page_leave.setStyleSheet("")
        self.page_leave.setObjectName("page_leave")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_leave)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_leave)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit_id = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_id.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_id.setReadOnly(True)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.horizontalLayout_4.addWidget(self.lineEdit_id)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_5.addWidget(self.lineEdit_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.dateTimeEdit_start = QtWidgets.QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit_start.setMinimumSize(QtCore.QSize(0, 30))
        self.dateTimeEdit_start.setObjectName("dateTimeEdit_start")
        self.horizontalLayout_6.addWidget(self.dateTimeEdit_start)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.dateTimeEdit_end = QtWidgets.QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit_end.setMinimumSize(QtCore.QSize(0, 30))
        self.dateTimeEdit_end.setObjectName("dateTimeEdit_end")
        self.horizontalLayout_7.addWidget(self.dateTimeEdit_end)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.pushButton_submit = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_submit.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_submit.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.horizontalLayout_9.addWidget(self.pushButton_submit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_leave)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableView_leave = QtWidgets.QTableView(self.groupBox_4)
        self.tableView_leave.setObjectName("tableView_leave")
        self.horizontalLayout_8.addWidget(self.tableView_leave)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.stackedWidget.addWidget(self.page_leave)
        self.page_record = QtWidgets.QWidget()
        self.page_record.setStyleSheet("")
        self.page_record.setObjectName("page_record")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.page_record)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_record)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tableView_record = QtWidgets.QTableView(self.groupBox_5)
        self.tableView_record.setObjectName("tableView_record")
        self.horizontalLayout_10.addWidget(self.tableView_record)
        self.horizontalLayout_11.addWidget(self.groupBox_5)
        self.stackedWidget.addWidget(self.page_record)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生端"))
        self.toolButton_leave.setText(_translate("MainWindow", "请假"))
        self.toolButton_record.setText(_translate("MainWindow", "考勤"))
        self.groupBox_3.setTitle(_translate("MainWindow", "请假申请"))
        self.label.setText(_translate("MainWindow", "请假人学号"))
        self.label_2.setText(_translate("MainWindow", "请假人姓名"))
        self.label_3.setText(_translate("MainWindow", "请假开始时间"))
        self.label_4.setText(_translate("MainWindow", "请假结束时间"))
        self.pushButton_submit.setText(_translate("MainWindow", "提交"))
        self.groupBox_4.setTitle(_translate("MainWindow", "请假记录"))
        self.groupBox_5.setTitle(_translate("MainWindow", "考勤记录"))
