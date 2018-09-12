import sys
from PyQt5.QtWidgets import *
from drawBlock import Game2048

class MainWindow(QMainWindow, Game2048):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setUp(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
