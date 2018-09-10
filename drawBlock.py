from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QFont, QTextOption
from PyQt5.QtCore import Qt, QRectF
from block import *
from constants import *
from time import sleep

class Game2048(QMainWindow):

    def __init__(self):
        super().__init__()
        # set window
        self.setGeometry(SIZE_CONSTANTS.WINDOW_LEFT, SIZE_CONSTANTS.WINDOW_TOP, SIZE_CONSTANTS.WINDOW_WIDTH, SIZE_CONSTANTS.WINDOW_HEIGHT)
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
        drawBlock = DrawBlock(self)
        drawBlock.drawBlocks()


class DrawBlock(QWidget):

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
        for y in range(0, 4):
            for x in range(0, 4):
                value = BLOCK_ARRAY.blocks[x][y].value # block value
                qp.setPen(COLOR_CONSTANTS.WHITE)  # set edge color
                qp.setBrush(COLOR_CONSTANTS.FILLS[value]) # set rect fill color
                rect = QRectF(SIZE_CONSTANTS.BLOCK_SIZE*x, SIZE_CONSTANTS.BLOCK_SIZE*y, SIZE_CONSTANTS.BLOCK_SIZE, SIZE_CONSTANTS.BLOCK_SIZE) # set rect
                qp.drawRect(rect) # draw rect
                if value != 0:
                    qp.setPen(COLOR_CONSTANTS.FONTS[value]) # set font color
                    qp.drawText(rect, str(value), textOption) # in rect draw value text

    def drawBlocks(self):
        self.move(50, SIZE_CONSTANTS.WINDOW_HEIGHT / 2 - SIZE_CONSTANTS.BLOCK_SIZE*2)
        self.resize(SIZE_CONSTANTS.BLOCK_SIZE*4, SIZE_CONSTANTS.BLOCK_SIZE*4)

    # x : column index, y : row index
    # 블럭이 있었던 위치는 0으로 세팅됩니다.
    # 블럭이 움직이고자 하는 위치에 블럭이 있다면 해당 블럭은 무시되고 새로운 블럭으로 세팅됩니다.
    # (움직이고자 하는 위치에 블럭이 있는건 별도로 체크하지 않는다)
    def moveBlock(self, direct, x, y):
        nx = x + DIRECT_CONSTANTS.DX[int(direct)]
        ny = y + DIRECT_CONSTANTS.DY[int(direct)]

        if(nx < 0 or 4 <= nx or ny < 0 or 4 <= ny):
            raise Exception("out of range")
        BLOCK_ARRAY.blocks[nx][ny].value = BLOCK_ARRAY.blocks[x][y].value
        BLOCK_ARRAY.blocks[x][y].value = 0
        
        # TODO 새로운 블럭들 그려주는 함수 추가


