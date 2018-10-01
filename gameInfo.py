from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QFont, QTextOption
from PyQt5.QtCore import Qt, QRectF, QTimer, QTime
from constants import *
from fileManager import FileManager


class GameInfo(QWidget):
    score = 0
    timer = QTimer()
    time = QTime(0, 0, 0)
    best = 0
    fileManager = FileManager()
    try:
        best = fileManager.readLineFile(CONSTANTS.INFO.FILE_DIRECT, CONSTANTS.INFO.FILE_NAME)
    except LookupError:
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

        qp.setPen(CONSTANTS.COLOR.WHITE)

        # score
        qp.setBrush(CONSTANTS.COLOR.GAME_INFO_NAME)
        nameRect = CONSTANTS.SIZE.GAME_INFO_SCORE_NAME
        qp.drawRect(nameRect)
        qp.setPen(CONSTANTS.COLOR.WHITE)
        qp.drawText(nameRect, str('SCORE'), textOption)

        qp.setBrush(CONSTANTS.COLOR.GAME_INFO_VALUE)
        valueRect = CONSTANTS.SIZE.GAME_INFO_SCORE_VALUE
        qp.drawRect(valueRect)
        qp.setPen(CONSTANTS.COLOR.WHITE)
        qp.drawText(valueRect, str(self.score), textOption)

        # timer
        qp.setBrush(CONSTANTS.COLOR.GAME_INFO_NAME)
        nameRect = CONSTANTS.SIZE.GAME_INFO_TIMER_NAME
        qp.drawRect(nameRect)
        qp.setPen(CONSTANTS.COLOR.WHITE)
        qp.drawText(nameRect, str('TIMER'), textOption)

        qp.setBrush(CONSTANTS.COLOR.GAME_INFO_VALUE)
        valueRect = CONSTANTS.SIZE.GAME_INFO_TIMER_VALUE
        qp.drawRect(valueRect)
        qp.setPen(CONSTANTS.COLOR.WHITE)
        qp.drawText(valueRect, str(self.time.toString("hh:mm:ss")), textOption)

        # best
        qp.setBrush(CONSTANTS.COLOR.GAME_INFO_BEST_NAME)
        nameRect = CONSTANTS.SIZE.GAME_INFO_BEST_NAME
        qp.drawRect(nameRect)
        qp.setPen(CONSTANTS.COLOR.WHITE)
        qp.drawText(nameRect, str('BEST'), textOption)

        qp.setBrush(CONSTANTS.COLOR.GAME_INFO_BEST_VALUE)
        valueRect = CONSTANTS.SIZE.GAME_INFO_BEST_VALUE
        qp.drawRect(valueRect)
        qp.setPen(CONSTANTS.COLOR.WHITE)
        qp.drawText(valueRect, str(self.best), textOption)

    def drawBlocks(self):
        self.move(CONSTANTS.SIZE.WINDOW_WIDTH / 2 + 100, CONSTANTS.SIZE.WINDOW_HEIGHT / 2 - 250)
        self.resize(CONSTANTS.SIZE.BLOCK_SIZE * 5, CONSTANTS.SIZE.BLOCK_SIZE * 5)

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

    # Best 갱신시 True 반환
    def setBest(self, best):
        if self.best < best:
            self.best = best
            self.fileManager.writeFile(CONSTANTS.INFO.FILE_DIRECT, CONSTANTS.INFO.FILE_NAME, best)
            return True
        return False

    def getBest(self):
        return self.best
