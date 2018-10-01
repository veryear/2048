from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QFont, QTextOption
from PyQt5.QtCore import Qt, QRectF
from block import *
from constants import *


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
                value = BLOCK_ARRAY.blocks[x][y].value  # block value
                qp.setPen(CONSTANTS.COLOR.WHITE)  # set edge color
                qp.setBrush(CONSTANTS.COLOR.FILLS[value])  # set rect fill color
                rect = QRectF(CONSTANTS.SIZE.BLOCK_SIZE * x, CONSTANTS.SIZE.BLOCK_SIZE * y, CONSTANTS.SIZE.BLOCK_SIZE,
                              CONSTANTS.SIZE.BLOCK_SIZE)  # set rect
                qp.drawRect(rect)  # draw rect
                if value != 0:
                    qp.setPen(CONSTANTS.COLOR.FONTS[value])  # set font color
                    qp.drawText(rect, str(value), textOption)  # in rect draw value text

    def drawBlocks(self):
        self.move(50, CONSTANTS.SIZE.WINDOW_HEIGHT / 2 - CONSTANTS.SIZE.BLOCK_SIZE * 2)
        self.resize(CONSTANTS.SIZE.BLOCK_SIZE * 4, CONSTANTS.SIZE.BLOCK_SIZE * 4)

    # x : column index, y : row index
    # 블럭이 있었던 위치는 0으로 세팅됩니다.
    # 블럭이 움직이고자 하는 위치에 블럭이 있다면 해당 블럭은 무시되고 새로운 블럭으로 세팅됩니다.
    # (움직이고자 하는 위치에 블럭이 있는건 별도로 체크하지 않는다)
    # value 값으로 블럭을 그려줍니다.
    def moveBlock(self, direct, x, y, value):

        flag = 0

        # UP
        if direct == 0:
            while y - 1 >= 0:
                if BLOCK_ARRAY.blocks[x][y - 1].value == 0:
                    BLOCK_ARRAY.blocks[x][y].value = 0
                    BLOCK_ARRAY.blocks[x][y - 1].value = value

                elif BLOCK_ARRAY.blocks[x][y - 1].value == value:
                    BLOCK_ARRAY.blocks[x][y - 1].value = value * 2
                    BLOCK_ARRAY.blocks[x][y].value = 0
                    flag = 1

                elif BLOCK_ARRAY.blocks[x][y - 1].value != value:
                    break

                y -= 1

        # RIGHT
        elif direct == 1:
            while x + 1 < 4:
                if BLOCK_ARRAY.blocks[x + 1][y].value == 0:
                    BLOCK_ARRAY.blocks[x][y].value = 0
                    BLOCK_ARRAY.blocks[x + 1][y].value = value

                elif BLOCK_ARRAY.blocks[x + 1][y].value == value:
                    BLOCK_ARRAY.blocks[x + 1][y].value = value * 2
                    BLOCK_ARRAY.blocks[x][y].value = 0
                    flag = 1

                elif BLOCK_ARRAY.blocks[x + 1][y].value != value:
                    break

                x += 1

        # DOWN
        elif direct == 2:
            while y + 1 < 4:
                if BLOCK_ARRAY.blocks[x][y + 1].value == 0:
                    BLOCK_ARRAY.blocks[x][y].value = 0
                    BLOCK_ARRAY.blocks[x][y + 1].value = value

                elif BLOCK_ARRAY.blocks[x][y + 1].value == value:
                    BLOCK_ARRAY.blocks[x][y + 1].value = value * 2
                    BLOCK_ARRAY.blocks[x][y].value = 0
                    flag = 1

                elif BLOCK_ARRAY.blocks[x][y + 1].value != value:
                    break

                y += 1

        # LEFT
        elif direct == 3:
            while x - 1 >= 0:
                if BLOCK_ARRAY.blocks[x - 1][y].value == 0:
                    BLOCK_ARRAY.blocks[x][y].value = 0
                    BLOCK_ARRAY.blocks[x - 1][y].value = value

                elif BLOCK_ARRAY.blocks[x - 1][y].value == value:
                    BLOCK_ARRAY.blocks[x - 1][y].value = value * 2
                    BLOCK_ARRAY.blocks[x][y].value = 0
                    flag = 1

                elif BLOCK_ARRAY.blocks[x - 1][y].value != value:
                    break

                x -= 1

        BLOCK_LIST.list1.append(x * 10 + y)
        if flag:
            BLOCK_LIST.list1.pop()

        self.update()
