import sys
from PyQt5.QtWidgets import *

class Game2048(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('2048')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game2048()
    sys.exit(app.exec_())
