# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ui_main_window import Ui_MainWindow
from ui_dialog_box import Ui_Dialog
from model import ManagerModel
from database import createConnection


class Window(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.managerModel = ManagerModel()
        self.ui.setupUi(self)
        self.show()


        self.ui.tableView.setModel(self.managerModel.model)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.pushButton_new.clicked.connect(self.openAddDialog)
        self.ui.pushButton_delete.clicked.connect(self.deleteContent)
        self.ui.pushButton_delete_all.clicked.connect(self.clearContents)

    
    def openAddDialog(self):
        """Open dialog box to add new information into database"""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.managerModel.addContent(dialog.data)
            self.ui.tableView.resizeColumnsToContents()


    def deleteContent(self):
        """Delete the selected information from the database."""
        row = self.ui.tableView.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected information?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.managerModel.deleteContent(row)


    def clearContents(self):
        """Remove all contacts from the database."""
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove all your information?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.managerModel.clearContents()
            



class AddDialog(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        self.ui_dialog = Ui_Dialog()
        self.data = None
        self.ui_dialog.setupUi(self)
        
        self.platformField = self.ui_dialog.lineEdit_platform
        self.loginField = self.ui_dialog.lineEdit_username
        self.passwordField = self.ui_dialog.lineEdit_password

        self.ui_dialog.buttonBox.accepted.connect(self.accept)
        self.ui_dialog.buttonBox.rejected.connect(self.reject)

    def accept(self):

        self.data = []
        for field in (self.platformField, self.loginField, self.passwordField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "error!",
                    f"you must provide valid information"
                )
                self.data = None
                return
            
            self.data.append(field.text())

        if not self.data:
            return

        super().accept()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    if not createConnection("accounts.sqlite"):
        sys.exit(1)

    Dialog = QtWidgets.QDialog()
    window = Window()
    sys.exit(app.exec_())
