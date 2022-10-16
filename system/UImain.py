import sys

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip

# 实例化
app = QApplication(sys.argv)
win = QWidget()

# 设置
win.setWindowTitle('system of sxy')
win.setWindowIcon(QIcon("D:\pythonStudy\python\system\Assets\图标.jpeg"))
QToolTip.setFont(QFont(''))
win.setToolTip('sxy system')

# 显示
win.show()
sys.exit(app.exec_())
