from PyQt5.QtCore import *
from constants import *
from keyboardInput import KeyboardInput
from drawBlock import DrawBlock
from gameInfo import GameInfo

class Game2048(object):
    keyboardInput = KeyboardInput()

    def setUp(self, MainWindow):
        super().__init__()

        # set window
        self.setGeometry(SIZE_CONSTANTS.WINDOW_LEFT, SIZE_CONSTANTS.WINDOW_TOP, SIZE_CONSTANTS.WINDOW_WIDTH,
                         SIZE_CONSTANTS.WINDOW_HEIGHT)
        self.setWindowTitle('2048')
        # init game
        self.initGame()
        # show UI
        self.show()

    def initGame(self):
        # set bg color
        self.setAutoFillBackground(True)
        p = self.palette()  # palette
        p.setColor(self.backgroundRole(), Qt.white)  # color white into bg
        self.setPalette(p)

        # draw 4x4 block
        self.drawBlock = DrawBlock(self)
        self.drawBlock.drawBlocks()

        # timer
        self.gameInfo = GameInfo(self)
        self.gameInfo.setTimer()
        self.gameInfo.drawBlocks()

    def keyPressEvent(self, event):
        direct = self.keyboardInput.getKey(event.key())
        # TODO 키보드 입력에 맞게 로직 태우기 -> 알고리즘 부분에서 사용해주세요
        # if(direct != DIRECT_CONSTANTS.NONE):
        #     self.drawBlock.moveBlock(direct, x, y, 새로운블럭값(value))