from PyQt5.QtWidgets import QMainWindow, QApplication

import sys

from widgets import main


class Register(QMainWindow, main.Ui_Main):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        self.setupUi(self)
        


def mainn():
    app = QApplication(sys.argv)
    register = Register()
    register.show()   
    app.exec_()


if __name__ == '__main__':
    mainn()