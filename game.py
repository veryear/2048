from PyQt5.QtCore import *
from constants import *
from keyboardInput import KeyboardInput
from drawBlock import DrawBlock
from gameInfo import GameInfo
from randomValue import RandomValue


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

        # Generate Random Values
        self.randomValue = RandomValue(self)
        self.randomValue.GenerValue()

        # timer & score & best
        self.gameInfo = GameInfo(self)
        self.gameInfo.setTimer()
        self.gameInfo.drawBlocks()

        # 값 세팅은 아래와 같이 해주시면 됩니다.
        # 필요하면 사용하시고 필요없는건 지워주시면 됩니다.
        # self.gameInfo.setScore(50)
        # self.gameInfo.setTime(1*60*60 + 59*60 + 52)
        # self.gameInfo.setBest(2048)

    def keyPressEvent(self, event):
        direct = self.keyboardInput.getKey(event.key())
