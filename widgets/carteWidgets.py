from PyQt5.QtWidgets import QMainWindow, QApplication
from widgets import carte
from widgets.mainWidgets import Register
from widgets.listedbWidgets import ViewList
import sys



class Accueil(QMainWindow, carte.Ui_Carte):
    def __init__(self, parent=None):
        super(Accueil, self).__init__(parent)
        self.setupUi(self)
        self.viewRegis_btn.clicked.connect(self.lancer_Register)
        self.viewList_btn.clicked.connect(self.lancer_ViewList)

    def lancer_Register(self):
        self.win = Register()
        self.win.show()
    
    def lancer_ViewList(self):
        self.win = ViewList()
        self.win.show()
