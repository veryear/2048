from PyQt5.QtCore import *
from constants import *
from keyboardInput import KeyboardInput
from drawBlock import DrawBlock
from gameInfo import GameInfo
from block import *
from random import *


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

        # Generate Random values
        self.x = 0
        self.y = 0
        cnt = 0
        while (cnt < 2):
            self.x = randrange(0, 4)
            self.y = randrange(0, 4)
            if BLOCK_ARRAY.blocks[self.x][self.y].value == 0:
                BLOCK_ARRAY.blocks[self.x][self.y].value = 2
                cnt += 1
        # BLOCK_ARRAY.blocks[self.x][self.y].value = 4

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
        # TODO 키보드 입력에 맞게 로직 태우기 -> 알고리즘 부분에서 사용해주세요
        key = self.keyboardInput.getKey(event.key())

        if (key != DIRECT_CONSTANTS.NONE):
            self.drawBlock.moveBlock(key, self.x, self.y, BLOCK_ARRAY.blocks[self.x][self.y].value)
            self.x = self.x + DIRECT_CONSTANTS.DX[int(key)]
            self.y = self.y + DIRECT_CONSTANTS.DY[int(key)]

        # BLOCK_ARRAY.blocks[1][1].value = 4

        # if(direct != DIRECT_CONSTANTS.NONE):
        #     self.drawBlock.moveBlock(direct, x, y, 새로운블럭값(value))
