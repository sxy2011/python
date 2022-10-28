import sys
import threading
import time
import _thread

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
class UI(QWidget):
    def __init__(self):
        super.__init__()
        self.app = QApplication(sys.argv)
        self.win = QWidget()

    def sitting(self):
        self.win.setWindowTitle('system of sxy')
        self.win.setWindowIcon(QIcon("D:\\pythonStudy\\python\\system\\Assets\\图标.jpeg"))
        self.win.setGeometry(300, 200, 400, 340)
        return self.win

    def sitting_exitButton(self):
        self.exit_ = QPushButton('关闭', self.win)
        self.exit_.move(300, 300)
        self.exit_.show()
        return self.exit_

    def show_(self):
        def job():
            time.sleep(100)

        _thread.start_new_thread(job, ())
        _thread.start_new_thread(job, ())
        job()
        self.win.show()
        sys.exit(self.app.exec_())
