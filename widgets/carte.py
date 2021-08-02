# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/carte.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Carte(object):
    def setupUi(self, Carte):
        Carte.setObjectName("Carte")
        Carte.resize(812, 583)
        Carte.setStyleSheet("QMainWindow\n"
"{\n"
"    background:#000\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Carte)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 781, 571))
        self.label.setStyleSheet("opacity:0.3")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/../assets/amoirie1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 0, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:rgb(123, 124, 124);\n"
"color:#fff;\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.viewRegis_btn = QtWidgets.QPushButton(self.centralwidget)
        self.viewRegis_btn.setGeometry(QtCore.QRect(160, 460, 131, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.viewRegis_btn.setFont(font)
        self.viewRegis_btn.setStyleSheet("background:#458b00;\n"
"color:#fff;\n"
" border:none;\n"
"border-radius:10px")
        self.viewRegis_btn.setObjectName("viewRegis_btn")
        self.viewList_btn = QtWidgets.QPushButton(self.centralwidget)
        self.viewList_btn.setGeometry(QtCore.QRect(530, 460, 131, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.viewList_btn.setFont(font)
        self.viewList_btn.setStyleSheet("background:#458b00;\n"
"color:#fff;\n"
"border:none;\n"
"border-radius:10px")
        self.viewList_btn.setObjectName("viewList_btn")
        Carte.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Carte)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 20))
        self.menubar.setObjectName("menubar")
        Carte.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Carte)
        self.statusbar.setObjectName("statusbar")
        Carte.setStatusBar(self.statusbar)

        self.retranslateUi(Carte)
        QtCore.QMetaObject.connectSlotsByName(Carte)

    def retranslateUi(self, Carte):
        _translate = QtCore.QCoreApplication.translate
        Carte.setWindowTitle(_translate("Carte", "Accueil"))
        self.label_2.setText(_translate("Carte", "BIENVENUE"))
        self.viewRegis_btn.setText(_translate("Carte", "Enregistrement"))
        self.viewList_btn.setText(_translate("Carte", "Action"))
import ressource_rc
