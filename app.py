import sys
from PyQt5.QtWidgets import *
from drawBlock import Game2048

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game2048()
    sys.exit(app.exec_())
