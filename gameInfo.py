from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QFont, QTextOption
from PyQt5.QtCore import Qt, QRectF, QTimer, QTime
from block import *
from constants import *


class GameInfo(QWidget):

    def paintEvent(self, event):
        qp = QPainter(self)

        # set font
        font = QFont()
        font.setPointSize(15)
        qp.setFont(font)

        # set font align center
        textOption = QTextOption()
        textOption.setAlignment(Qt.AlignCenter)

        qp.setPen(COLOR_CONSTANTS.WHITE)  # set edge color
        qp.setBrush(COLOR_CONSTANTS.GAME_INFO_VALUE)  # set rect fill color
        rect = QRectF(0, 0, SIZE_CONSTANTS.BLOCK_SIZE*2, SIZE_CONSTANTS.BLOCK_SIZE)  # set rect
        qp.drawRect(rect)  # draw rect
        qp.setPen(COLOR_CONSTANTS.WHITE)  # set font color
        # qp.drawRect(rect, str('SCORE'), textOption)
        qp.drawText(rect, str(self.time.toString("hh:mm:ss")), textOption)  # in rect draw value text

    def drawBlocks(self):
        self.move(SIZE_CONSTANTS.WINDOW_WIDTH/2 + 100, SIZE_CONSTANTS.WINDOW_HEIGHT/2 - 100)
        self.resize(SIZE_CONSTANTS.BLOCK_SIZE * 4, SIZE_CONSTANTS.BLOCK_SIZE * 4)

    def setTimer(self):
        self.timer = QTimer(self)
        self.time = QTime(0, 0, 0)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

    def updateTime(self):
        self.time = self.time.addSecs(1)
        self.update()
