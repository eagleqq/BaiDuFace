import os
from PyQt5.QtWidgets import QMainWindow, QWidget

from project.gui.admin.ui_class import Ui_Class
from project.gui.admin.ui_course import Ui_Course


class CourseWidget(QWidget, Ui_Course):

    def __init__(self, parent=None):
        super(CourseWidget, self).__init__(parent)
        self.setupUi(self)
        self._initVariables()
        self._initWidget()
        self._initConnect()

    def _initVariables(self):
        pass

    def _initWidget(self):
        pass

    def _initConnect(self):
        pass


