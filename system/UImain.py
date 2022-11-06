import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel


class UI_class(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        dk = app.desktop()
        self.setWindowTitle('system of sxy')
        self.setWindowIcon(QIcon("D:\\pythonStudy\\python\\system\\Assets\\图标.jpeg"))
        self.resize(600, 400)
        self.exitButton()
        self.loginLabel()
    
    def exitButton(self):
        self.exit_ = QPushButton('关闭', self)
        self.exit_.show()
        self.exit_.move(525, 375)
        self.show()
        self.exit_.clicked.connect(self.close)
    
    def closeEvent(self, QCloseEvent):
        self.exit_q = QMessageBox.question(self, '?', '你确定要关闭吗?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if self.exit_q == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
    
    def loginLabel(self):
        self.login_l = QLabel('登录', self)
        self.login_l.resize(30, 50)
        self.login_l.move(1, 1)
        self.login_l.show()

app = QApplication(sys.argv)
win = UI_class()
win.initUI()
sys.exit(app.exec_())
