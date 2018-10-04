from PyQt5.QtWidgets import *
from random import *
from constants import *


# BLOCK class
class BLOCK:
    value = 0  # block value


# BLOCK array class
class BLOCK_ARRAY:
    # set BLOCK array 4*4
    blocks = [[BLOCK()] * 4 for i in range(4)]

    for y in range(0, 4):
        for x in range(0, 4):
            blocks[x][y] = BLOCK()


# random block class
class RandomBlock(QWidget):
    # Make Random Block
    def makeRandomBlock(self):
        # check blank block
        chck = 0
        for x in range(0, 4):
            for y in range(0, 4):
                if BLOCK_ARRAY.blocks[x][y].value == CONSTANTS.BLANK_BLOCKS.blank:
                    chck = 1
                    break
            if chck:
                break
        # if it has not blank block
        if chck == 0:
            raise Exception("No blank blocks")

        while (1):
            x = randrange(0, 4)
            y = randrange(0, 4)
            if BLOCK_ARRAY.blocks[x][y].value == CONSTANTS.BLANK_BLOCKS.blank:
                BLOCK_ARRAY.blocks[x][y].value = 2
                break
