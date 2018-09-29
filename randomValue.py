from PyQt5.QtWidgets import *
from random import *
from block import *


class RandomValue(QWidget):

    # Generate Random Values
    def GenerValue(self):
        self.x = 0
        self.y = 0
        cnt = 0
        while (cnt < 2):
            self.x = randrange(0, 4)
            self.y = randrange(0, 4)
            if BLOCK_ARRAY.blocks[self.x][self.y].value == 0:
                BLOCK_ARRAY.blocks[self.x][self.y].value = 2
                cnt += 1
