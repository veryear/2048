import keyboard
from constants import DIRECT_CONSTANTS

class KeyboardInput:

    def getKey(self):
        while True:
            if keyboard.is_pressed('up'):
                 return DIRECT_CONSTANTS.UP
            elif keyboard.is_pressed('down'):
                 return DIRECT_CONSTANTS.DOWN
            elif keyboard.is_pressed('left'):
                 return DIRECT_CONSTANTS.LEFT
            elif keyboard.is_pressed('right'):
                 return DIRECT_CONSTANTS.RIGHT
