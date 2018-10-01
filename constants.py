from PyQt5.QtGui import QColor
from PyQt5.QtCore import QRectF


class COLOR_CONSTANTS:
    FONTS = {}  # font color
    FILLS = {}  # rect fill color

    WHITE = QColor(255, 255, 255)
    BLACK = QColor(0, 0, 0)

    FONTS[0] = BLACK
    FONTS[2] = BLACK
    FONTS[4] = BLACK
    FONTS[8] = WHITE
    FONTS[16] = WHITE
    FONTS[32] = WHITE
    FONTS[64] = WHITE
    FONTS[128] = WHITE
    FONTS[256] = WHITE
    FONTS[512] = WHITE
    FONTS[1024] = WHITE
    FONTS[2048] = WHITE

    FILLS[0] = QColor(200, 200, 200)
    FILLS[2] = QColor(253, 247, 234)
    FILLS[4] = QColor(246, 223, 170)
    FILLS[8] = QColor(237, 190, 86)
    FILLS[16] = QColor(255, 102, 0)
    FILLS[32] = QColor(253, 69, 16)
    FILLS[64] = QColor(253, 28, 16)
    FILLS[128] = QColor(137, 199, 236)
    FILLS[256] = QColor(65, 168, 223)
    FILLS[512] = QColor(42, 142, 223)
    FILLS[1024] = QColor(27, 86, 184)
    FILLS[2048] = QColor(62, 67, 135)

    GAME_INFO_NAME = QColor(210, 117, 117)
    GAME_INFO_VALUE = QColor(233, 185, 185)

    GAME_INFO_BEST_NAME = QColor(69, 124, 194)
    GAME_INFO_BEST_VALUE = QColor(161, 189, 223)


class DIRECT_CONSTANTS:
    NONE = -1
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    # 시계방향. (UP, RIGHT, DOWN, LEFT)
    DX = [0, 1, 0, -1]  # column
    DY = [-1, 0, 1, 0]  # row


class SIZE_CONSTANTS:
    # one block size (150 x 150)
    BLOCK_SIZE = 150

    # window size
    WINDOW_LEFT = 300
    WINDOW_TOP = 150
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800

    # (left, up, width, height)
    GAME_INFO_SCORE_NAME = QRectF(0, 0, BLOCK_SIZE, BLOCK_SIZE)
    GAME_INFO_SCORE_VALUE = QRectF(BLOCK_SIZE, 0, BLOCK_SIZE * 2, BLOCK_SIZE)

    GAME_INFO_TIMER_NAME = QRectF(0, BLOCK_SIZE + 10, BLOCK_SIZE, BLOCK_SIZE)
    GAME_INFO_TIMER_VALUE = QRectF(BLOCK_SIZE, BLOCK_SIZE + 10, BLOCK_SIZE * 2, BLOCK_SIZE)

    GAME_INFO_BEST_NAME = QRectF(BLOCK_SIZE / 2, BLOCK_SIZE * 2 + 50, BLOCK_SIZE / 4 * 3, BLOCK_SIZE / 4 * 3)
    GAME_INFO_BEST_VALUE = QRectF(BLOCK_SIZE / 4 * 5, BLOCK_SIZE * 2 + 50, BLOCK_SIZE * (1 + 1 / 4),
                                  BLOCK_SIZE / 4 * 3)


class BLANK_BLOCKS:
    blank = 0
