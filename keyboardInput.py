from PyQt5.QtCore import Qt
from constants import DIRECT_CONSTANTS

class KeyboardInput:

    def getKey(self, key):
        if key == Qt.Key_Up:
            return DIRECT_CONSTANTS.UP
        elif key == Qt.Key_Down:
            return DIRECT_CONSTANTS.DOWN
        elif key == Qt.Key_Left:
            return DIRECT_CONSTANTS.LEFT
        elif key == Qt.Key_Right:
            return DIRECT_CONSTANTS.RIGHT
        else:
            return DIRECT_CONSTANTS.NONE
