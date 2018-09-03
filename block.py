from PyQt5.QtGui import QColor

# BLOCK class
class BLOCK:
    value = 0   # block value

# BLOCK array class
class BLOCK_ARRAY:

    # set BLOCK array 4*4
    blocks = [[BLOCK()]*4 for i in range(4)]

class COLOR:

    FILLS = {}

    def __init__(self):

        self.FILLS[0] = QColor(255, 255, 255)
        self.FILLS[2] = QColor(253, 247, 234)
        self.FILLS[4] = QColor(246, 223, 170)
        self.FILLS[8] = QColor(237, 190, 86)
        self.FILLS[16] = QColor(255, 102, 0)
        self.FILLS[32] = QColor(253, 69, 16)
        self.FILLS[64] = QColor(253, 28, 16)
        self.FILLS[128] = QColor(137, 199, 236)
        self.FILLS[256] = QColor(65, 168, 223)
        self.FILLS[512] = QColor(42, 142, 223)
        self.FILLS[1024] = QColor(27, 86, 184)
        self.FILLS[2048] = QColor(62, 67, 135)