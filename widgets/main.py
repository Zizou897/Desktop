# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 600)
        Main.setStyleSheet("background:#000")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 321, 41))
        font = QtGui.QFont()
        font.setFamily("KacstBook")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("background:#71bc3b;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"border-radius:10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.nom = QtWidgets.QLineEdit(self.centralwidget)
        self.nom.setGeometry(QtCore.QRect(60, 140, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nom.setFont(font)
        self.nom.setStyleSheet("border: 2px solid #4a8c0d;\n"
"padding: 10px;\n"
"border-radius:7px;\n"
"color:#fff\n"
"")
        self.nom.setClearButtonEnabled(False)
        self.nom.setObjectName("nom")
        self.prenom = QtWidgets.QLineEdit(self.centralwidget)
        self.prenom.setGeometry(QtCore.QRect(340, 140, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.prenom.setFont(font)
        self.prenom.setStyleSheet("border: 2px solid #4a8c0d;\n"
"padding: 10px;\n"
"border-radius:7px;\n"
"color:#fff\n"
"")
        self.prenom.setObjectName("prenom")
        self.placeBirth = QtWidgets.QLineEdit(self.centralwidget)
        self.placeBirth.setGeometry(QtCore.QRect(340, 240, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.placeBirth.setFont(font)
        self.placeBirth.setStyleSheet("border: 2px solid #4a8c0d;\n"
"padding: 10px;\n"
"border-radius:7px;\n"
"color:#fff\n"
"")
        self.placeBirth.setObjectName("placeBirth")
        self.homme = QtWidgets.QRadioButton(self.centralwidget)
        self.homme.setGeometry(QtCore.QRect(140, 240, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.homme.setFont(font)
        self.homme.setStyleSheet("color:#fff")
        self.homme.setObjectName("homme")
        self.femme = QtWidgets.QRadioButton(self.centralwidget)
        self.femme.setGeometry(QtCore.QRect(190, 240, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.femme.setFont(font)
        self.femme.setStyleSheet("color:#fff")
        self.femme.setChecked(True)
        self.femme.setObjectName("femme")
        self.genre = QtWidgets.QLabel(self.centralwidget)
        self.genre.setEnabled(True)
        self.genre.setGeometry(QtCore.QRect(60, 240, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.genre.setFont(font)
        self.genre.setStyleSheet("color:#fff")
        self.genre.setScaledContents(False)
        self.genre.setObjectName("genre")
        self.annuler = QtWidgets.QPushButton(self.centralwidget)
        self.annuler.setGeometry(QtCore.QRect(130, 470, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.annuler.setFont(font)
        self.annuler.setStyleSheet("\n"
"border: none;\n"
"border-radius:8px;\n"
"background-color:rgb(255, 38, 0);\n"
"color:#fff;\n"
"gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.33 rgba(0, 0, 0, 255), stop:0.34 rgba(255, 30, 30, 255), stop:0.66 rgba(255, 0, 0, 255), stop:0.67 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255));")
        self.annuler.setObjectName("annuler")
        self.valider = QtWidgets.QPushButton(self.centralwidget)
        self.valider.setGeometry(QtCore.QRect(470, 470, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.valider.setFont(font)
        self.valider.setStyleSheet("QPushButton\n"
"{\n"
"    border: none;\n"
"    border-radius:8px;\n"
"    background-color:rgb(0, 170, 0);\n"
"    color:#fff;\n"
"    transition: 0.3s\n"
"}\n"
"")
        self.valider.setObjectName("valider")
        self.dateBirth = QtWidgets.QDateEdit(self.centralwidget)
        self.dateBirth.setGeometry(QtCore.QRect(60, 320, 211, 41))
        self.dateBirth.setStyleSheet("border: 2px solid #4a8c0d;\n"
"padding: 10px;\n"
"border-radius:5px;\n"
"padding-left:10px;\n"
"color:#fff\n"
"")
        self.dateBirth.setObjectName("dateBirth")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(570, 140, 211, 221))
        self.photo.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.photo.setAutoFillBackground(False)
        self.photo.setStyleSheet("")
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap(":/img/assets/pngwing.com (1).png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.phone = QtWidgets.QLineEdit(self.centralwidget)
        self.phone.setGeometry(QtCore.QRect(340, 320, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.phone.setFont(font)
        self.phone.setStyleSheet("border: 2px solid #4a8c0d;\n"
"padding: 10px;\n"
"border-radius:7px;\n"
"color:#fff\n"
"")
        self.phone.setObjectName("phone")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Enrolement"))
        self.label.setText(_translate("Main", "Enrolement"))
        self.nom.setPlaceholderText(_translate("Main", "Nom"))
        self.prenom.setPlaceholderText(_translate("Main", "Prénom"))
        self.placeBirth.setPlaceholderText(_translate("Main", "Lieu De Naissance"))
        self.homme.setText(_translate("Main", "H"))
        self.femme.setText(_translate("Main", "F"))
        self.genre.setText(_translate("Main", "Genre :"))
        self.annuler.setText(_translate("Main", "Rafraichir"))
        self.valider.setText(_translate("Main", "Valider"))
        self.phone.setPlaceholderText(_translate("Main", "Téléphone"))
import ressource_rc
