import sys
import threading
import time
import _thread

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox

# 实例化
app = QApplication(sys.argv)
win = QWidget()

# 设置
win.setWindowTitle('system of sxy')
win.setWindowIcon(QIcon("D:\\pythonStudy\\python\\system\\Assets\\图标.jpeg"))
win.setGeometry(300, 200, 400, 340)
exit_ = QPushButton('关闭', win)
exit_.move(300, 300)
exit_.show()


def job():
    time.sleep(100)


_thread.start_new_thread(job, exit_function())
_thread.start_new_thread(job, ())
job()

# 显示
win.show()
sys.exit(app.exec_())
