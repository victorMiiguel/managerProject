# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from ui_login import Ui_login
from ui_main_window import Ui_MainWindow
from ui_dialog_box import Ui_Dialog
from model import ManagerModel
from database import createConnection


class LoginWindow(QMainWindow, Ui_login):
    
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.uiLogin = Ui_login()
        self.uiLogin.setupUi(self)
        self.uiMainWindow = Window()
        self.login_data = None
        self.show()
        #
        #   FUNCTIONS
        #
        self.uiLogin.frame_error.hide()
        self.uiLogin.pushButton_close_error.clicked.connect(lambda: self.uiLogin.frame_error.hide())
        self.uiLogin.pushButton_enter.clicked.connect(self.checkFields)



    def checkFields(self):
        """Checks login fields for the correct information"""
        self.username_error = ""
        self.password_error = ""

        def showMessage(self, message):
            """Show error message"""
            self.uiLogin.frame_error.show()
            self.uiLogin.label_error.setText(self.message)
            

        
        if not self.uiLogin.lineEdit_login.text():
            self.username_error = " Username Empty. "
        else:
            self.username_error = ""

        if not self.uiLogin.lineEdit_pwd.text():
            self.password_error = " Password Empty. "
        else:
            self.password_error = ""
        
        if self.uiLogin.lineEdit_login.text() != "Admin":
            self.username_error = " Invalid Username "
        else:
            self.username_error = ""
        
        if self.uiLogin.lineEdit_pwd.text() != "1234":
            self.password_error = " Invalid Password "
        else:
            self.password_error = ""

        if self.username_error + self.password_error != "":
            self.message = self.username_error + self.password_error
            showMessage(self, self.message)
        else:
            self.close()
            self.uiMainWindow.show()




class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.uiLogin = Ui_login()
        self.ui = Ui_MainWindow()
        self.managerModel = ManagerModel()
        self.ui.setupUi(self)
        #
        #   FUNCTIONS
        #
        self.ui.tableView.setModel(self.managerModel.model)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.pushButton_new.clicked.connect(self.openAddDialog)
        self.ui.pushButton_delete.clicked.connect(self.deleteContent)
        self.ui.pushButton_delete_all.clicked.connect(self.clearContents)

    

    def openAddDialog(self):
        """Open dialog box to add new data into database"""
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
        """Remove all data from the database."""
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
        super(AddDialog, self).__init__(parent=parent)
        self.uiDialog = Ui_Dialog()
        self.data = None
        self.uiDialog.setupUi(self)
        #
        #   FUNCTIONS
        #
        self.platformField = self.uiDialog.lineEdit_platform
        self.loginField = self.uiDialog.lineEdit_username
        self.passwordField = self.uiDialog.lineEdit_password

        self.uiDialog.buttonBox.accepted.connect(self.accept)
        self.uiDialog.buttonBox.rejected.connect(self.reject)



    def accept(self):
        """Accept and Save data into the database."""
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

    login = LoginWindow()
    window = Window()
    Dialog = QtWidgets.QDialog()
    sys.exit(app.exec_())
