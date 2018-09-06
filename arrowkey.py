from msvcrt import getch

def right():
    print('right')

def left():
    print('left')

def up():
    print('up')

def down():
    print('down')

key = ord(getch())  # input arrow keys

if key == 77:  # right arrow
    right()
elif key == 75:  # left arrow
    left()
elif key == 72:  # up arrow
    up()
elif key == 80:  # down arrow
    down()