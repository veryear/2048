from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QFont, QTextOption
from PyQt5.QtCore import Qt, QRectF
from block import BLOCK_ARRAY, COLOR
from keyboardInput import KeyboardInput

class Game2048(QMainWindow):

    WINDOW_LEFT = 300
    WINDOW_TOP = 150
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800

    blockArray = BLOCK_ARRAY()
    keyboardInput = KeyboardInput()

    def __init__(self):
        super().__init__()
        # set window
        self.setGeometry(self.WINDOW_LEFT, self.WINDOW_TOP, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle('2048')
        # set setting
        self.initGameSetting()
        # set game screen
        self.initGameScreen()
        # show UI
        self.show()
        self.playGame()

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

    def initGameSetting(self):
        self.blockArray = BLOCK_ARRAY()

    def playGame(self):
        key = self.keyboardInput.getKey()
        print(key)

class DrawBlock(QWidget, BLOCK_ARRAY):

    # one block size (150 x 150)
    BLOCK_SIZE = 150
    COLOR = COLOR()

    def paintEvent(self, event):
        qp = QPainter(self)

        # set font
        font = QFont()
        font.setPointSize(30)
        qp.setFont(font)

        # set font align center
        textOption = QTextOption()
        textOption.setAlignment(Qt.AlignCenter)

        # draw 4x4 block rectangle
        for i in range(0, 4):
            for j in range(0, 4):
                value = self.blocks[j][i].value # block value
                qp.setPen(Qt.white)  # set edge color
                qp.setBrush(self.COLOR.FILLS[value]) # set rect fill color
                rect = QRectF(self.BLOCK_SIZE*j, self.BLOCK_SIZE*i, self.BLOCK_SIZE, self.BLOCK_SIZE) # set rect
                qp.drawRect(rect) # draw rect
                if value != 0:
                    qp.setPen(self.COLOR.FONTS[value]) # set font color
                    qp.drawText(rect, str(value), textOption) # in rect draw value text
