from PyQt5.QtCore import Qt
from constants import CONSTANTS


class KeyboardInput:

    def getKey(self, key):
        if key == Qt.Key_Up:
            return CONSTANTS.DIRECT.UP
        elif key == Qt.Key_Down:
            return CONSTANTS.DIRECT.DOWN
        elif key == Qt.Key_Left:
            return CONSTANTS.DIRECT.LEFT
        elif key == Qt.Key_Right:
            return CONSTANTS.DIRECT.RIGHT
        else:
            return CONSTANTS.DIRECT.NONE
