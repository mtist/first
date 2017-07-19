import sys 
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QBasicTimer, QSize

UNACTIVE = 'bo1.png'
GOOD = 'bo3.png'
BAD = 'b02.png'
TIME = 30


class MyWidget(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.now = 0

		self.timer = QBasicTimer()
		self.step = 0

		grid = QGridLayout()
		grid.setSpacing(10)

		self.holes = []

		x, y = 0, 0
		for i in range(9):
			self.holes.append(QPushButton('U', self))
			self.holes[i].setFlat(True)
			self.holes[i].setIcon(QIcon(UNACTIVE))
			self.holes[i].setIconSize(QSize(200, 200))

			grid.addWidget(self.holes[i], x, y)
			
			if x < 2:
				x += 1
			else:
				y += 1 
				x = 0

		self.setLayout(grid)
		self.setWindowTitle('UI, not GUI')
		self.setGeometry(100, 100, 720, 480)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MyWidget()
	sys.exit(app.exec_())