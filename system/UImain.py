import sys
import function
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox

# 实例化
app = QApplication(sys.argv)
win = QWidget()

# 设置
fun = function.function()
win.setWindowTitle('system of sxy')
win.setWindowIcon(QIcon("D:\\pythonStudy\\python\\system\\Assets\\图标.jpeg"))
QToolTip.setFont(QFont('隶书', 15))
win.setToolTip('sxy system')
win.setGeometry(300, 230, 400, 340)
exit_ = QPushButton('关闭', win)
exit_.move(300, 300)
exit_.show()
exit_.clicked.connect(fun.exit_1())

# 显示
win.show()
sys.exit(app.exec_())
