from PyQt5.QtWidgets import *
from random import *
from block import *


class RandomValue(QWidget):

    # Generate Random Values
    def GenerValue(self, cnt):
        self.x = 0
        self.y = 0

        while (cnt > 0):
            self.x = randrange(0, 4)
            self.y = randrange(0, 4)

            if BLOCK_ARRAY.blocks[self.x][self.y].value == 0:
                BLOCK_ARRAY.blocks[self.x][self.y].value = 2
                BLOCK_LIST.list1.append(self.x * 10 + self.y)
                cnt -= 1
