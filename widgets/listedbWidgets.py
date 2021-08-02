from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets
import sys
import sqlite3
import os
from . import listedb



class ViewList(QMainWindow, listedb.Ui_ListDB):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.donnee()
        self.button()
    

    def button(self):
        self.buttonSearch.clicked.connect(self.rechercheNom)
        self.buttonSuppr.clicked.connect(self.supprimer)


    def donnee(self):
        db = sqlite3.connect(os.path.join(os.path.dirname("__file__"), "storage/database.db"))
        cursor = db.cursor()
        command = ''' SELECT * FROM data '''
        resultat = cursor.execute(command)
        self.table.setRowCount(0)

        for row_number, row_data in enumerate(resultat):
            self.table.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                donne = QtWidgets.QTableWidgetItem(str(data))
                self.table.setItem(row_number, colum_number, donne)


    def rechercheNom(self):
        search = str(self.searchNom.text())
        if search == '':
            self.donnee()
        else:
            db = sqlite3.connect(os.path.join(os.path.dirname("__file__"), "storage/database.db"))
            cursor = db.cursor()
            command = ''' SELECT * FROM data WHERE Nom LIKE ? '''
            resultat = cursor.execute(command, [search])
            self.table.setRowCount(0)
        
            for row_number, row_data in enumerate(resultat):
                self.table.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    donne = QtWidgets.QTableWidgetItem(str(data))
                    self.table.setItem(row_number, colum_number, donne)
    
    def supprimer(self):
        line = self.table.currentRow()
        id_line = self.table.item(line,0).text()
        answer = QMessageBox.question(self, "Cool", "Voulez vous supprimer ?", QMessageBox.Yes / QMessageBox.No)

        if answer == 16384:
            db = sqlite3.connect(os.path.join(os.path.dirname("__file__"), "storage/database.db"))
            cursor = db.cursor()
            command = ''' DELETE FROM data WHERE Id=? '''
            cursor.execute(command, (id_line))
            db.commit()
            self.data()




