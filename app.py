import sys
from PyQt5.QtWidgets import *
from drawBlock import Game2048

def main():
    app = QApplication(sys.argv)
    game = Game2048()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()