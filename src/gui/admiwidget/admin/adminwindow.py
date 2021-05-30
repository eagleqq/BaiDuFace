import os
from PyQt5.QtWidgets import QMainWindow

from src.gui.admiwidget.admin.Infowidget import InfoWidget
from src.gui.admiwidget.admin.facewidget import FaceWidget
from src.gui.admiwidget.admin.signmanagerwidget import SignManagerWidget
from src.gui.admiwidget.admin.ui_admin import Ui_Admin


class AdminWindow(QMainWindow, Ui_Admin):

    def __init__(self, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.setupUi(self)
        self.initWidget()
        self.initConnect()

    def initWidget(self):
        self.stackedWidget.setCurrentWidget(self.page_home)
        self.info_widget = InfoWidget()
        self.face_widget = FaceWidget()
        self.sign_manager_widget = SignManagerWidget()
        self.stackedWidget.addWidget(self.info_widget)
        self.stackedWidget.addWidget(self.face_widget)
        self.stackedWidget.addWidget(self.sign_manager_widget)

    def initConnect(self):
        self.toolButton_home.clicked.connect(self.slotCheckoutHome)  # 首页
        self.toolButton_personal_info.clicked.connect(self.slotCheckoutPersonalIno)  # 个人信息
        self.toolButton_face.clicked.connect(self.slotCheckoutFace)  # 人脸注册
        self.toolButton_leave_manage.clicked.connect(self.slotCheckoutLeave)  # 请假管理
        self.toolButton_record.clicked.connect(self.slotCheckoutRecord)  # 打卡记录
        self.toolButton_setting.clicked.connect(self.slotCheckoutSetting)  # 打开设置

    def setUp(self):
        """
        由外部程序初始化
        :return:
        """
        self.face_widget.setUp()

    def slotCheckoutHome(self):
        self.stackedWidget.setCurrentWidget(self.page_home)

    def slotCheckoutPersonalIno(self):
        self.stackedWidget.setCurrentWidget(self.info_widget)

    def slotCheckoutFace(self):
        self.stackedWidget.setCurrentWidget(self.face_widget)

    def slotCheckoutLeave(self):
        pass

    def slotCheckoutRecord(self):
        self.stackedWidget.setCurrentWidget(self.sign_manager_widget)

    def slotCheckoutSetting(self):
        pass


