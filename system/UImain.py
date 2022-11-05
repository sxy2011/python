import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox


# noinspection PyTypeChecker
class UI_class(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('system of sxy')
        self.setWindowIcon(QIcon("D:\\pythonStudy\\python\\system\\Assets\\图标.jpeg"))
        self.resize(600, 400)
        QToolTip.setFont(QFont('隶书', 15))
        self.setToolTip('sxy system')
        self.exit_ = QPushButton('关闭', self)
        self.exit_.show()
        self.exit_.move(525, 375)
        self.show()
        self.exit_.clicked.connect(self.close)

    def closeEvent(self, QCloseEvent):
        self.exit_q = QMessageBox.question(self, '?', '你确定要关闭吗?', QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)


app = QApplication(sys.argv)
win = UI_class()
win.initUI()
sys.exit(app.exec_())
