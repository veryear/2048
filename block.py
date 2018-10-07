from PyQt5.QtWidgets import *
from random import *
from constants import *


# BLOCK class
class BLOCK:
    # block value
    value = 0


# BLOCK array class
class BLOCK_ARRAY:
    # set BLOCK array 4*4
    blocks = [[BLOCK()] * 4 for i in range(4)]

    for y in range(0, 4):
        for x in range(0, 4):
            blocks[x][y] = BLOCK()


# random block class
class RandomBlock(QWidget):
    # blankBLOCK list
    blankBlock_list = []

    # # check blank blocks or Not
    def isBlankBlock(self, x, y):
        if BLOCK_ARRAY.blocks[x][y].value == CONSTANTS.BLANK_BLOCKS.blank:
            return True
        else:
            return False

    # Make Random Block
    def makeRandomBlock(self):

        block = RandomBlock(self)

        # put BLANKBLOCK's (x*10 + y) value in blankBlock_list
        for x in range(0, 4):
            for y in range(0, 4):
                if block.isBlankBlock(x, y):
                    RandomBlock.blankBlock_list.append(x * 10 + y)

        # has not BLANCKBLOCK
        if len(RandomBlock.blankBlock_list) == 0:
            # "No blank blocks" message
            raise Exception("No blank blocks")
        # has BLANCKBLOCK
        else:
            # make random block
            blankBlock_list_idx = randrange(0, len(RandomBlock.blankBlock_list))
            x = int(RandomBlock.blankBlock_list[blankBlock_list_idx] / 10)
            y = int(RandomBlock.blankBlock_list[blankBlock_list_idx] % 10)
            BLOCK_ARRAY.blocks[x][y].value = 2

            # blankBlock_list's data delete
            del RandomBlock.blankBlock_list[:]
