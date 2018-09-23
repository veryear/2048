from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QFont, QTextOption
from PyQt5.QtCore import Qt, QRectF, QTimer, QTime
from constants import *


class GameInfo(QWidget):
    score = 0
    timer = QTimer()
    time = QTime(0, 0, 0)
    best = 0

    def paintEvent(self, event):
        qp = QPainter(self)

        # set font
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        qp.setFont(font)

        # set font align center
        textOption = QTextOption()
        textOption.setAlignment(Qt.AlignCenter)

        qp.setPen(COLOR_CONSTANTS.WHITE)

        # score
        qp.setBrush(COLOR_CONSTANTS.GAME_INFO_NAME)
        nameRect = SIZE_CONSTANTS.GAME_INFO_SCORE_NAME
        qp.drawRect(nameRect)
        qp.setPen(COLOR_CONSTANTS.WHITE)
        qp.drawText(nameRect, str('SCORE'), textOption)

        qp.setBrush(COLOR_CONSTANTS.GAME_INFO_VALUE)
        valueRect = SIZE_CONSTANTS.GAME_INFO_SCORE_VALUE
        qp.drawRect(valueRect)
        qp.setPen(COLOR_CONSTANTS.WHITE)
        qp.drawText(valueRect, str(self.score), textOption)

        # timer
        qp.setBrush(COLOR_CONSTANTS.GAME_INFO_NAME)
        nameRect = SIZE_CONSTANTS.GAME_INFO_TIMER_NAME
        qp.drawRect(nameRect)
        qp.setPen(COLOR_CONSTANTS.WHITE)
        qp.drawText(nameRect, str('TIMER'), textOption)

        qp.setBrush(COLOR_CONSTANTS.GAME_INFO_VALUE)
        valueRect = SIZE_CONSTANTS.GAME_INFO_TIMER_VALUE
        qp.drawRect(valueRect)
        qp.setPen(COLOR_CONSTANTS.WHITE)
        qp.drawText(valueRect, str(self.time.toString("hh:mm:ss")), textOption)

        # best
        qp.setBrush(COLOR_CONSTANTS.GAME_INFO_BEST_NAME)
        nameRect = SIZE_CONSTANTS.GAME_INFO_BEST_NAME
        qp.drawRect(nameRect)
        qp.setPen(COLOR_CONSTANTS.WHITE)
        qp.drawText(nameRect, str('BEST'), textOption)

        qp.setBrush(COLOR_CONSTANTS.GAME_INFO_BEST_VALUE)
        valueRect = SIZE_CONSTANTS.GAME_INFO_BEST_VALUE
        qp.drawRect(valueRect)
        qp.setPen(COLOR_CONSTANTS.WHITE)
        qp.drawText(valueRect, str(self.best), textOption)

    def drawBlocks(self):
        self.move(SIZE_CONSTANTS.WINDOW_WIDTH / 2 + 100, SIZE_CONSTANTS.WINDOW_HEIGHT / 2 - 250)
        self.resize(SIZE_CONSTANTS.BLOCK_SIZE * 5, SIZE_CONSTANTS.BLOCK_SIZE * 5)

    def setTimer(self):
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

    def updateTime(self):
        self.time = self.time.addSecs(1)
        self.update()

    def setTime(self, sec):
        self.time = QTime(sec / (60 * 60), (sec % (60 * 60)) / 60, sec % 60)

    def getTime(self):
        return self.time

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def setBest(self, best):
        self.best = best

    def getBest(self):
        return self.best
