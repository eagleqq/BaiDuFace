# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_admin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(1030, 649)
        Admin.setMinimumSize(QtCore.QSize(0, 0))
        Admin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(Admin)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("font: 16pt \"新宋体\";")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.toolButton_home = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_home.setMinimumSize(QtCore.QSize(100, 40))
        self.toolButton_home.setObjectName("toolButton_home")
        self.verticalLayout.addWidget(self.toolButton_home)
        spacerItem1 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.toolButton_personal_info = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_personal_info.setMinimumSize(QtCore.QSize(100, 40))
        self.toolButton_personal_info.setObjectName("toolButton_personal_info")
        self.verticalLayout.addWidget(self.toolButton_personal_info)
        spacerItem2 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.toolButton_face = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_face.setMinimumSize(QtCore.QSize(100, 40))
        self.toolButton_face.setObjectName("toolButton_face")
        self.verticalLayout.addWidget(self.toolButton_face)
        spacerItem3 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.toolButton_leave_manage = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_leave_manage.setMinimumSize(QtCore.QSize(100, 40))
        self.toolButton_leave_manage.setObjectName("toolButton_leave_manage")
        self.verticalLayout.addWidget(self.toolButton_leave_manage)
        spacerItem4 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.toolButton_record = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_record.setMinimumSize(QtCore.QSize(100, 40))
        self.toolButton_record.setObjectName("toolButton_record")
        self.verticalLayout.addWidget(self.toolButton_record)
        spacerItem5 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.toolButton_setting = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_setting.setMinimumSize(QtCore.QSize(100, 40))
        self.toolButton_setting.setObjectName("toolButton_setting")
        self.verticalLayout.addWidget(self.toolButton_setting)
        spacerItem6 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_2)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_home)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.label = QtWidgets.QLabel(self.page_home)
        self.label.setStyleSheet("font: 20pt \"新宋体\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.stackedWidget.addWidget(self.page_home)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        Admin.setCentralWidget(self.centralwidget)
        self.exportLogAction = QtWidgets.QAction(Admin)
        self.exportLogAction.setObjectName("exportLogAction")
        self.aboutAction = QtWidgets.QAction(Admin)
        self.aboutAction.setObjectName("aboutAction")

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "管理员页面"))
        self.toolButton_home.setText(_translate("Admin", "  首页  "))
        self.toolButton_personal_info.setText(_translate("Admin", "个人信息"))
        self.toolButton_face.setText(_translate("Admin", "人脸注册"))
        self.toolButton_leave_manage.setText(_translate("Admin", "请假管理"))
        self.toolButton_record.setText(_translate("Admin", "打卡记录"))
        self.toolButton_setting.setText(_translate("Admin", "打卡设置"))
        self.label.setText(_translate("Admin", "欢迎来到后台管理系统"))
        self.exportLogAction.setText(_translate("Admin", "导出日志"))
        self.aboutAction.setText(_translate("Admin", "关于"))

