from PyQt5.QtWidgets import QMainWindow, QApplication

import sys

from widgets import carte
from regist import Register

class Accueil(QMainWindow, carte.Ui_Carte):
    def __init__(self, parent=None):
        super(Accueil, self).__init__(parent)
        self.setupUi(self)
        self.viewRegis_btn.clicked.connect(Register)



def mainn():
    app = QApplication(sys.argv)
    accueil = Accueil()
    accueil.show()
    app.exec_()
        



if __name__ == '__main__':
    mainn()