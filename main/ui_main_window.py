# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 900)
        MainWindow.setMinimumSize(QtCore.QSize(500, 200))
        MainWindow.setMaximumSize(QtCore.QSize(700, 500))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_top.setStyleSheet("background-color: rgb(41, 41, 59);\n"
"color: rgb(255, 207, 0);")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_new = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_new.setMinimumSize(QtCore.QSize(110, 28))
        self.pushButton_new.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.pushButton_new.setFont(font)
        self.pushButton_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_new.setStyleSheet("QPushButton {\n"
"    margin-left: 10px;\n"
"    background-color: rgb(100, 100, 100);\n"
"    border-radius: 5px;\n"
"    border-left: none;\n"
"    border-right: 2px solid rgb(0, 0, 0);\n"
"    border-bottom: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 207, 0);\n"
"    border-right: 2px solid rgb(255, 120, 0);\n"
"    border-bottom: 2px solid rgb(255, 120, 0);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_new.setObjectName("pushButton_new")
        self.horizontalLayout.addWidget(self.pushButton_new)
        self.pushButton_delete = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_delete.setMinimumSize(QtCore.QSize(110, 28))
        self.pushButton_delete.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_delete.setStyleSheet("QPushButton {\n"
"    margin-left: 10px;\n"
"    background-color: rgb(100, 100, 100);\n"
"    border-radius: 5px;\n"
"    border-left: none;\n"
"    border-right: 2px solid rgb(0, 0, 0);\n"
"    border-bottom: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 207, 0);\n"
"    border-right: 2px solid rgb(255, 120, 0);\n"
"    border-bottom: 2px solid rgb(255, 120, 0);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout.addWidget(self.pushButton_delete)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_delete_all = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_delete_all.setMinimumSize(QtCore.QSize(110, 28))
        self.pushButton_delete_all.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.pushButton_delete_all.setFont(font)
        self.pushButton_delete_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_delete_all.setStyleSheet("QPushButton {\n"
"    margin-right: 10px;\n"
"    background-color: rgb(100, 100, 100);\n"
"    border-radius: 5px;\n"
"    border-left: none;\n"
"    border-right: 2px solid rgb(0, 0, 0);\n"
"    border-bottom: 2px solid rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 207, 0);\n"
"    border-right: 2px solid rgb(255, 120, 0);\n"
"    border-bottom: 2px solid rgb(255, 120, 0);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_delete_all.setObjectName("pushButton_delete_all")
        self.horizontalLayout.addWidget(self.pushButton_delete_all)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_center = QtWidgets.QFrame(self.centralwidget)
        self.frame_center.setMinimumSize(QtCore.QSize(700, 0))
        self.frame_center.setStyleSheet("background-color: rgb(41, 41, 59);")
        self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_center)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_header = QtWidgets.QFrame(self.frame_center)
        self.frame_header.setMinimumSize(QtCore.QSize(0, 65))
        self.frame_header.setStyleSheet("background-image: url(:/top_bar/Images/top_bar2.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setObjectName("frame_header")
        self.verticalLayout_2.addWidget(self.frame_header)
        self.tableView = QtWidgets.QTableView(self.frame_center)
        self.tableView.setMinimumSize(QtCore.QSize(500, 0))
        self.tableView.setMaximumSize(QtCore.QSize(950, 16777215))
        self.tableView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableView.setStyleSheet("QTableView {\n"
"    color: rgb(225, 225, 255);\n"
"    border: 2px solid rgb(41, 41, 65);\n"
"    background-color: rgb(41, 41, 59);\n"
"}\n"
"QTableView:hover {\n"
"    \n"
"    background-color: rgb(41, 41, 55);\n"
"}")
        self.tableView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.verticalLayout.addWidget(self.frame_center)
        self.frame_bottom = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_bottom.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_bottom)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_bottom)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-image: url(:/bottom_bar/Images/background_bottom.png);\n"
"color: rgb(255, 207, 0);\n"
"\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Password Manager"))
        self.pushButton_new.setText(_translate("MainWindow", "New"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_delete_all.setText(_translate("MainWindow", "Delete All"))
        self.label.setText(_translate("MainWindow", "Designed by Miguel Victor"))
import resources_main_window
