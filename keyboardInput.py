import keyboard #Using module keyboard
class KeyboardInput:
    def right(self):
        print('right')

    def left(self):
        print('left')

    def up(self):
        print('up')

    def down(self):
        print('down')

    def getKey(self):

        while True:  # making a loop
            if keyboard.is_pressed(keyboard.KEY_UP):  # if key 'q' is pressed
                 return keyboard.KEY_UP
