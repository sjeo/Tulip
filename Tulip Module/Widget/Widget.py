from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget
from Widget.ui2.untitled import Ui_socket
from Widget.ui2.unititled_functions import SOCKETFUNCTIONS


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.m_Position = None
        self.m_flag = None
        self.ui = Ui_socket()
        self.ui.setupUi(self)
        socketfunctions = SOCKETFUNCTIONS(self)
        socketfunctions.socket_basic()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框和标题栏
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)  # 更改窗口位置
            event.accept()
            return

    def mouseReleaseEvent(self, event):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
