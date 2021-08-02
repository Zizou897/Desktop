# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/listedb.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListDB(object):
    def setupUi(self, ListDB):
        ListDB.setObjectName("ListDB")
        ListDB.resize(804, 586)
        font = QtGui.QFont()
        font.setPointSize(9)
        ListDB.setFont(font)
        ListDB.setWindowOpacity(1.0)
        ListDB.setStyleSheet("background:#000;")
        self.centralwidget = QtWidgets.QWidget(ListDB)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(0, 170, 0);\n"
"color:#fff;\n"
"border-radius:10px")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(50, 200, 691, 241))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.table.setFont(font)
        self.table.setStyleSheet("font: 7pt \"Sans Serif\";\n"
"\n"
"background:#fff")
        self.table.setObjectName("table")
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        self.searchNom = QtWidgets.QLineEdit(self.centralwidget)
        self.searchNom.setGeometry(QtCore.QRect(410, 140, 121, 31))
        self.searchNom.setStyleSheet("background:#fff")
        self.searchNom.setText("")
        self.searchNom.setObjectName("searchNom")
        self.buttonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSearch.setGeometry(QtCore.QRect(530, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.buttonSearch.setFont(font)
        self.buttonSearch.setStyleSheet("color:#fff;\n"
"background-color:rgb(148, 123, 200);\n"
"border:none;\n"
"border-radius:0 10px 10px 0;")
        self.buttonSearch.setObjectName("buttonSearch")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#fff")
        self.label_2.setObjectName("label_2")
        self.buttonSuppr = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSuppr.setGeometry(QtCore.QRect(200, 480, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.buttonSuppr.setFont(font)
        self.buttonSuppr.setStyleSheet("background:rgb(255, 85, 0);\n"
"color:#fff;\n"
"border:none;\n"
"border-radius:5px\n"
"")
        self.buttonSuppr.setObjectName("buttonSuppr")
        self.buttonApercu = QtWidgets.QPushButton(self.centralwidget)
        self.buttonApercu.setGeometry(QtCore.QRect(380, 480, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.buttonApercu.setFont(font)
        self.buttonApercu.setStyleSheet("background:#947bc8;\n"
"color:#fff;\n"
"border:none;\n"
"border-radius:5px\n"
"")
        self.buttonApercu.setObjectName("buttonApercu")
        self.buttonModif = QtWidgets.QPushButton(self.centralwidget)
        self.buttonModif.setGeometry(QtCore.QRect(560, 480, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.buttonModif.setFont(font)
        self.buttonModif.setStyleSheet("background:#55aa00;\n"
"color:#fff;\n"
"border:none;\n"
"border-radius:5px\n"
"")
        self.buttonModif.setObjectName("buttonModif")
        ListDB.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListDB)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 20))
        self.menubar.setObjectName("menubar")
        ListDB.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListDB)
        self.statusbar.setObjectName("statusbar")
        ListDB.setStatusBar(self.statusbar)

        self.retranslateUi(ListDB)
        QtCore.QMetaObject.connectSlotsByName(ListDB)

    def retranslateUi(self, ListDB):
        _translate = QtCore.QCoreApplication.translate
        ListDB.setWindowTitle(_translate("ListDB", "Liste"))
        self.label.setText(_translate("ListDB", "Liste Des Inscrits"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("ListDB", "Id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("ListDB", "Nom"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("ListDB", "Prenom"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("ListDB", "Genre"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("ListDB", "Téléphone"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("ListDB", "Date de Naissance"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("ListDB", "Lieu de Naissance"))
        self.buttonSearch.setText(_translate("ListDB", "Rechercher"))
        self.label_2.setText(_translate("ListDB", "Recherche par Nom"))
        self.buttonSuppr.setText(_translate("ListDB", "Supprimer"))
        self.buttonApercu.setText(_translate("ListDB", "Aperçu"))
        self.buttonModif.setText(_translate("ListDB", "Modifier"))
