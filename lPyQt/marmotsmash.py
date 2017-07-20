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
            self.holes[i].clicked.connect(self.smash)

            grid.addWidget(self.holes[i], x, y)
            
            if x < 2:
                x += 1
            else:
                y += 1 
                x = 0

        self.count = QLabel('0')
        self.time = QLabel(str(TIME))
        self.runBt = QPushButton('Start')
        self.runBt.clicked.connect(self.startGame)

        grid.addWidget(self.count, y, 0)
        grid.addWidget(self.runBt, y, 1)
        grid.addWidget(self.time, y, 2)


        self.setLayout(grid)
        self.setWindowTitle('UI, not GUI')
        self.setGeometry(100, 100, 720, 480)
        self.show()

    def showHim(self):
        number = randint(0, 9)
        kind = randint(0, 1)
        if kind:
            self.holes[number].setText('G')
            self.holes[number].setIcon(QIcon(GOOD))
        else:
            self.holes[number].setText('B')
            self.holes[number].setIcon(QIcon(BAD))

        self.now = number

    def clearHim(self):
        self.holes[self.now].setText('U')
        self.holes[self.now].setIcon(QIcon(UNACTIVE))

    def timerEvent(self, e):
        self.clearHim()
        self.showHim()

        if self.step >= TIME * 2:
            self.timer.stop()
            self.runBt.setEnabled(True)
            self.time.setText(str(TIME))
            self.step = 0
            self.clearHim()
            return

        self.step += 1

        if self.step % 2:
            time = int(self.time.text()) - 1
            self.time.setText(str(time))
    
    def startGame(self):
        time = TIME * 1000 // 60
        self.timer.start(time, self)
        self.count.setText('0')
        self.runBt.setEnabled(False)

    def smash(self):
        sender = self.sender()
        if sender.text() == 'B':
            self.clearHim()
            count = int(self.count.text()) + 1
            self.count.setText(str(count))
        elif sender.text() == 'G':
            self.clearHim()
            count = int(self.count.text()) - 1
            self.count.setText(str(count))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())