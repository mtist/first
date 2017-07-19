import sys 
from PyQt5.QtWidgets import QApplication, QWidget

class MyWidget(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('UI, not GUI')
		self.setGeometry(100, 100, 720, 480)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MyWidget()
	sys.exit(app.exec_())