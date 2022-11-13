import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QHBoxLayout, QLineEdit


class UI_class(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		dk = app.desktop()
		QWidget.raise_(self)
		self.setWindowTitle('system of sxy')
		self.setWindowIcon(QIcon("D:\\pythonStudy\\python\\system\\Assets\\图标.jpeg"))
		self.resize(600, 400)
		self.move(dk.width() / 2 - self.width() / 2, dk.height() / 2 - self.height() / 2)
		self.createButton_absoluteness('关闭', 525, 375, 70, 20, self.close())
		self.createLabel_absoluteness('登录', 30, 50, 50, 50)
		self.show()
	
	def createButton_absoluteness(self, text=str, x=int, y=int, width=int, height=int, con=any):
		self.btn = QPushButton(text, self)
		self.btn.show()
		self.btn.resize(width, height)
		self.btn.move(x, y)
		self.btn.clicked.connect(con)
	
	def createLabel_absoluteness(self, text=str, x=int, y=int, width=int, height=int):
		self.label = QLabel(text, self)
		self.label.resize(width, height)
		self.label.move(x, y)
		self.label.show()
	
	def createLineEdit_absoluteness(self, x=int, y=int, width=int, height=int):
		code = QLineEdit(self)
		code.resize(width, height)
		code.move(x, y)
		code.show()
	
	def createButton_relatively(self, text=str, x=int, y=int, width=int, height=int, con=any):
		self.btn_control = QHBoxLayout(self)
		self.btn = QPushButton(text, self)
		self.btn_control.addWidget(self)
		self.btn.show()
		self.btn.resize(width, height)
		self.btn.move(x, y)
		self.btn.clicked.connect(con)
	
	def closeEvent(self, QCloseEvent):
		self.exit_q = QMessageBox.question(self, '?', '你确定要关闭吗?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if self.exit_q == QMessageBox.Yes:
			QCloseEvent.accept()
		else:
			QCloseEvent.ignore()


app = QApplication(sys.argv)
win = UI_class()
win.initUI()
sys.exit(app.exec_())
