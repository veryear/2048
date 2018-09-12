from PyQt5.QtGui import QColor

class COLOR_CONSTANTS:

    FONTS = {} # font color
    FILLS = {} # rect fill color

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

class DIRECT_CONSTANTS:

    NONE = -1
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    # 시계방향. (UP, RIGHT, DOWN, LEFT)
    DX = [0, 1, 0, -1] # column
    DY = [-1, 0, 1, 0] # row

class SIZE_CONSTANTS:

    # one block size (150 x 150)
    BLOCK_SIZE = 150

    # window size
    WINDOW_LEFT = 300
    WINDOW_TOP = 150
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800