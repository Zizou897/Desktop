from PyQt5.QtWidgets import QMainWindow, QApplication
from widgets.carteWidgets import Accueil
import sys





def mainn():
    app = QApplication(sys.argv)
    accueil = Accueil()
    accueil.show()
    app.exec_()
        



if __name__ == '__main__':
    mainn()