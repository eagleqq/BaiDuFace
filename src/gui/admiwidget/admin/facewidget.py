import os

import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu

from src.core.adminsql import AdminSql
from src.core.faceinterface import FaceInterface
from src.core.studentsql import StudentSql
from src.gui.admiwidget.admin.ui_face import Ui_Face
from src.gui.admiwidget.registerthread import RegisterThread


class FaceWidget(QWidget, Ui_Face):

    def __init__(self, parent=None):
        super(FaceWidget, self).__init__(parent)
        self.setupUi(self)
        self.facesdk = FaceInterface()

        self._initVariables()
        self._initWidget()
        self._initConnect()

        # 摄像头读取线程
        self.cameraReadThread = RegisterThread()
        self.cameraReadThread.signalFrame.connect(self.slotUpdateImage)
        self.cameraReadThread.signalResult.connect(self.slotUpdateResult)

        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  # 允许右键产生子菜单
        self.tableWidget.customContextMenuRequested.connect(self.contextMenuEvent)  # 右键菜单

    def setUp(self):
        self.cameraReadThread.threadStart()

    def _initVariables(self):
        StudentSql.sql_init()
        StudentSql.creat_table()

    def _initWidget(self):
        intValidator = QIntValidator()
        self.lineEdit_id.setValidator(intValidator)

        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        header = ["学号", "姓名", "是否上传"]
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.updateStudentTableData()

    def _initConnect(self):
        self.pushButton_add_student.clicked.connect(self._add_student)
        self.pushButton_add_face.clicked.connect(self._add_face)

    def updateStudentTableData(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        student_list = StudentSql.select_all()
        print(student_list)
        user_list = self.facesdk.getGroupUsers()
        for student in student_list:
            if str(student[0]) in user_list:
                self._append_to_table(student[0], student[1], "已上传")
            else:
                self._append_to_table(student[0], student[1], "未上传")

    def _add_student(self):
        id = self.lineEdit_id.text()
        name = self.lineEdit_name.text()
        if id == "" or name == "":
            QMessageBox.warning(self, "错误", "基本信息不能为空")
            return
        StudentSql.insert(id, name, False)
        self._append_to_table(id, name, "未上传")
        QMessageBox.information(self, "成功", "添加成功")
        self.lineEdit_name.setText("")
        self.lineEdit_id.setText("")

    def _append_to_table(self, id, name, has_upload):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        font = QFont()
        font.setPointSize(13)
        id_item = QTableWidgetItem(str(id))
        id_item.setTextAlignment(Qt.AlignCenter)
        id_item.setFont(font)
        name_item = QTableWidgetItem(name)
        name_item.setTextAlignment(Qt.AlignCenter)
        name_item.setFont(font)
        has_upload_item = QTableWidgetItem(has_upload)
        has_upload_item.setTextAlignment(Qt.AlignCenter)
        has_upload_item.setFont(font)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, id_item)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, name_item)
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, has_upload_item)

    def _add_face(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            QMessageBox.warning(self, "错误", "未选中学生")
            return
        self.cameraReadThread.addFaceFlag = True

    def showImgToLabel(self, frame):
        """
        显示图片到qt label上
        :param frame:  图片
        :return:
        """
        result_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        qtImg = QImage(result_frame.data,
                       result_frame.shape[1],
                       result_frame.shape[0],
                       QImage.Format_RGB888)
        self.label_pic.setScaledContents(True)
        self.label_pic.setPixmap(QPixmap.fromImage(qtImg))

    def slotUpdateImage(self, frame):
        self.showImgToLabel(frame)

    def slotUpdateResult(self, msg):
        """
        人脸拍照完成，开始注册
        :param msg:
        :return:
        """
        print("slotUpdateResult")
        print(msg)
        self.cameraReadThread.addFaceFlag = False
        try:
            row = self.tableWidget.currentRow()
            id = self.tableWidget.item(row, 0).text()
            StudentSql.update_uploadFace_by_id(id, True)
            self.tableWidget.item(row, 2).setText("已上传")
            register_face = open('./data/image/register_face.png', 'rb').read()
            self.facesdk.addUser(id, register_face)
            QMessageBox.information(self, '注册', '学号为{}人脸注册成功!'.format(id), QMessageBox.Yes)
            self.updateStudentTableData()
        except Exception as e:
            QMessageBox.information(self, '注册', '人脸注册失败，请重试! \n{}'.format(str(e)), QMessageBox.Yes)

    def contextMenuEvent(self, pos):
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        menu = QMenu()
        item_del = menu.addAction(u"删除")
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        if action == item_del:
            sid = self.tableWidget.item(row_num, 0).text()
            ret = QMessageBox.information(self, '删除', '确认删除学号{}!'.format(sid),
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ret == QMessageBox.Yes:
                print("删除")
                try:
                    ret = StudentSql.delete_by_id(sid)
                    print(ret)
                    self.facesdk.deleteUser(sid)
                    QMessageBox.information(self, '删除', '删除成功!', QMessageBox.Yes)
                except Exception as e:
                    QMessageBox.information(self, '删除', '删除失败！{}!'.format(str(e)), QMessageBox.Yes)
                self.updateStudentTableData()
        else:
            return