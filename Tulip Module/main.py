from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.ui_functions import UIFUNCTIONS
from ui.ui_main import Ui_MainWindow  # 假设生成的UI类名为Ui_MainWindow

Left, Top, Right, Bottom, LeftTop, RightTop, LeftBottom, RightBottom = range(8)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.styleSheet()
        self.m_Position = None
        self.m_flag = None
        self.Direction = None
        self._mpos = None
        self._pressed = None
        self.position = None
        self.Margins = 10
        # 初始化UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 将MainWindow实例作为参数传递
        uifunctions = UIFUNCTIONS(self)
        uifunctions.uibasic()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框和标题栏
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.position = event.pos()
            xPos, yPos = self.position.x(), self.position.y()
            wm, hm = self.width() - self.Margins, self.height() - self.Margins
            if xPos <= self.Margins and yPos <= self.Margins:
                # 左上角
                self.Direction = LeftTop
                self.setCursor(Qt.SizeFDiagCursor)
                self._pressed = True
            elif wm <= xPos <= self.width() and hm <= yPos <= self.height():
                # 右下角
                self.Direction = RightBottom
                self.setCursor(Qt.SizeFDiagCursor)
                self._pressed = True
            elif wm <= xPos and yPos <= self.Margins:
                # 右上角
                self.Direction = RightTop
                self.setCursor(Qt.SizeBDiagCursor)
                self._pressed = True
            elif xPos <= self.Margins and hm <= yPos:
                # 左下角
                self.Direction = LeftBottom
                self.setCursor(Qt.SizeBDiagCursor)
                self._pressed = True
            elif 0 <= xPos <= self.Margins <= yPos <= hm:
                # 左边
                self.Direction = Left
                self.setCursor(Qt.SizeHorCursor)
                self._pressed = True
            elif wm <= xPos <= self.width() and self.Margins <= yPos <= hm:
                # 右边
                self.Direction = Right
                self.setCursor(Qt.SizeHorCursor)
                self._pressed = True
            elif wm >= xPos >= self.Margins >= yPos >= 0:
                # 上面
                self.Direction = Top
                self.setCursor(Qt.SizeVerCursor)
                self._pressed = True
            elif self.Margins <= xPos <= wm and hm <= yPos <= self.height():
                # 下面
                self.Direction = Bottom
                self.setCursor(Qt.SizeVerCursor)
                self._pressed = True
        if event.button() == Qt.LeftButton and not self._pressed:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)  # 更改窗口位置
            event.accept()
            return
        if Qt.LeftButton and self._pressed:
            self._mpos = event.pos()
            self._resizeWidget(self.position)
            return

    def mouseReleaseEvent(self, event):
        self.m_flag = False
        self._pressed = False
        self.Direction = None
        self.setCursor(QCursor(Qt.ArrowCursor))

    def _resizeWidget(self, position):
        if self.Direction is None:
            return
        mpos = self._mpos - position
        xPos, yPos = mpos.x(), mpos.y()
        geometry = self.geometry()
        x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
        if self.Direction == LeftTop:  # 左上角
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
        elif self.Direction == RightBottom:  # 右下角
            if w + xPos > self.minimumWidth():
                w += xPos
            if h + yPos > self.minimumHeight():
                h += yPos
            self.position = self._mpos
        elif self.Direction == RightTop:  # 右上角
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            if w + xPos > self.minimumWidth():
                w += xPos
            self.position = self._mpos
        elif self.Direction == LeftBottom:  # 左下角
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h + yPos > self.minimumHeight():
                h += yPos
            self.position = self._mpos
        elif self.Direction == Left:  # 左边
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            else:
                return
        elif self.Direction == Right:  # 右边
            if w + xPos > self.minimumWidth():
                w += xPos
                self.position = self._mpos
            else:
                return
        elif self.Direction == Top:  # 上面
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            else:
                return
        elif self.Direction == Bottom:  # 下面
            if h + yPos > self.minimumHeight():
                y = y
                h += yPos
                self.position = self._mpos
            else:
                return
        self.setGeometry(x, y, w, h)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyleSheet("""
            QMenu {
                background-color: rgb(37, 41, 48);
                color: rgb(113, 126, 149);
            }
            QMenu::item {
                padding: 5px 10px;
                color: #ffffff;
            }
            QMenu::item:selected {
                background-color: #333333;
            }
            QMenu::separator {
                height: 1px;
                background-color: #555555;
                margin: 4px 0px 4px 10px;
            }
            QMenu::icon {
                margin-right: 10px;
            }
        """)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
