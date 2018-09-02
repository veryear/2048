from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class Game2048(QMainWindow):

    WINDOW_LEFT = 300
    WINDOW_TOP = 150
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800

    def __init__(self):
        super().__init__()
        # set window
        self.setGeometry(self.WINDOW_LEFT, self.WINDOW_TOP, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle('2048')
        # set game screen
        self.initGameScreen()
        # show UI
        self.show()

    def initGameScreen(self):

        # set bg color
        self.setAutoFillBackground(True)
        p = self.palette()  # palette
        p.setColor(self.backgroundRole(), Qt.white) # color white into bg
        self.setPalette(p)

        # draw 4x4 block
        self.drawBlock = DrawBlock(self)
        self.drawBlock.move(50, self.WINDOW_HEIGHT / 2 - self.drawBlock.BLOCK_SIZE*2)
        self.drawBlock.resize(self.drawBlock.BLOCK_SIZE*4, self.drawBlock.BLOCK_SIZE*4)


class DrawBlock(QWidget):

    # one block size (150 x 150)
    BLOCK_SIZE = 150

    def paintEvent(self, event):
        qp = QPainter(self)

        # edge color
        qp.setPen(Qt.white)

        # fill color
        qp.setBrush(Qt.darkRed)

        # draw 4x4 block rectangle
        for i in range(0, 4):
            for j in range(0, 4):
                qp.drawRect(self.BLOCK_SIZE*i, self.BLOCK_SIZE*j, self.BLOCK_SIZE, self.BLOCK_SIZE)