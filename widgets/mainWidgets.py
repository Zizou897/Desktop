from PyQt5.QtWidgets import QDialog, QApplication,QMainWindow
import sys
from . import main



class Register(QMainWindow, main.Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


