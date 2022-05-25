# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'habitos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(808, 592)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -10, 811, 561))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"background-color: qlineargradient(spread:pad, x1:0.233, y1:0.784091, x2:1, y2:0, stop:0 rgba(39, 39, 39, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.menu = QLabel(self.frame)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(60, 0, 751, 91))
        self.menu.setStyleSheet(u"font: 87 30pt \"Arial Black\";\n"
"background-color:#999;\n"
"border:1px solid white;\n"
"border-radius: 5px;\n"
"")
        self.lista = QLabel(self.frame)
        self.lista.setObjectName(u"lista")
        self.lista.setGeometry(QRect(400, 90, 241, 41))
        self.lista.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"margin: 10px;\n"
"color: white;")
        self.btnagreagar = QPushButton(self.frame)
        self.btnagreagar.setObjectName(u"btnagreagar")
        self.btnagreagar.setGeometry(QRect(120, 340, 181, 23))
        self.btnagreagar.setStyleSheet(u"QPushButton{\n"
"	display: block;\n"
"	border-radius: 2px;\n"
"	border: 1px solid white;\n"
"	width: 60px;\n"
"	padding: 3px;\n"
"	color: white;\n"
"	background-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #70b231;\n"
"}")
        self.lbnombre = QLabel(self.frame)
        self.lbnombre.setObjectName(u"lbnombre")
        self.lbnombre.setGeometry(QRect(30, 180, 141, 21))
        self.lbnombre.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: white;")
        self.lbdesde = QLabel(self.frame)
        self.lbdesde.setObjectName(u"lbdesde")
        self.lbdesde.setGeometry(QRect(30, 210, 131, 20))
        self.lbdesde.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: white;")
        self.lbhasta = QLabel(self.frame)
        self.lbhasta.setObjectName(u"lbhasta")
        self.lbhasta.setGeometry(QRect(30, 240, 131, 20))
        self.lbhasta.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: white;")
        self.lbinicio = QLabel(self.frame)
        self.lbinicio.setObjectName(u"lbinicio")
        self.lbinicio.setGeometry(QRect(30, 270, 131, 20))
        self.lbinicio.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: white;")
        self.lbhasta_2 = QLabel(self.frame)
        self.lbhasta_2.setObjectName(u"lbhasta_2")
        self.lbhasta_2.setGeometry(QRect(30, 300, 131, 20))
        self.lbhasta_2.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: white;")
        self.txtnombre = QLineEdit(self.frame)
        self.txtnombre.setObjectName(u"txtnombre")
        self.txtnombre.setGeometry(QRect(190, 180, 171, 20))
        self.txtnombre.setStyleSheet(u"QLineEdit {\n"
"	background-color: #ccc;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1px solid #70b231;\n"
"}")
        self.txtdesde = QLineEdit(self.frame)
        self.txtdesde.setObjectName(u"txtdesde")
        self.txtdesde.setGeometry(QRect(190, 210, 171, 20))
        self.txtdesde.setStyleSheet(u"QLineEdit {\n"
"	background-color: #ccc;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1px solid #70b231;\n"
"}")
        self.txthasta = QLineEdit(self.frame)
        self.txthasta.setObjectName(u"txthasta")
        self.txthasta.setGeometry(QRect(190, 240, 171, 20))
        self.txthasta.setStyleSheet(u"QLineEdit {\n"
"	background-color: #ccc;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1px solid #70b231;\n"
"}")
        self.txtinicio = QLineEdit(self.frame)
        self.txtinicio.setObjectName(u"txtinicio")
        self.txtinicio.setGeometry(QRect(190, 270, 171, 20))
        self.txtinicio.setStyleSheet(u"QLineEdit {\n"
"	background-color: #ccc;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1px solid #70b231;\n"
"}")
        self.txtfechahasta = QLineEdit(self.frame)
        self.txtfechahasta.setObjectName(u"txtfechahasta")
        self.txtfechahasta.setGeometry(QRect(190, 300, 171, 20))
        self.txtfechahasta.setStyleSheet(u"QLineEdit {\n"
"	background-color: #ccc;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1px solid #70b231;\n"
"}")
        self.btneliminar = QPushButton(self.frame)
        self.btneliminar.setObjectName(u"btneliminar")
        self.btneliminar.setGeometry(QRect(120, 380, 181, 23))
        self.btneliminar.setStyleSheet(u"QPushButton {\n"
"	display: block;\n"
"	border-radius: 2px;\n"
"	border: 1px solid white;\n"
"	width: 60px;\n"
"	padding: 3px;\n"
"	color: white;\n"
"	background-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #70b231;\n"
"}")
        self.btnmostrar = QPushButton(self.frame)
        self.btnmostrar.setObjectName(u"btnmostrar")
        self.btnmostrar.setGeometry(QRect(120, 460, 181, 23))
        self.btnmostrar.setStyleSheet(u"QPushButton {\n"
"	display: block;\n"
"	border-radius: 2px;\n"
"	border: 1px solid white;\n"
"	width: 60px;\n"
"	padding: 3px;\n"
"	color: white;\n"
"	background-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #70b231;\n"
"}")
        self.btneditar = QPushButton(self.frame)
        self.btneditar.setObjectName(u"btneditar")
        self.btneditar.setGeometry(QRect(120, 420, 181, 23))
        self.btneditar.setStyleSheet(u"QPushButton {\n"
"	display: block;\n"
"	border-radius: 2px;\n"
"	border: 1px solid white;\n"
"	width: 60px;\n"
"	padding: 3px;\n"
"	color: white;\n"
"	background-color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #70b231;\n"
"}")
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(410, 130, 381, 411))
        self.plainTextEdit.setStyleSheet(u"font: 75 8pt \"Arial\";")
        self.lblclave = QLabel(self.frame)
        self.lblclave.setObjectName(u"lblclave")
        self.lblclave.setGeometry(QRect(30, 150, 71, 16))
        self.lblclave.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: white;")
        self.txtclave = QLineEdit(self.frame)
        self.txtclave.setObjectName(u"txtclave")
        self.txtclave.setGeometry(QRect(190, 150, 171, 20))
        self.txtclave.setStyleSheet(u"QLineEdit {\n"
"	background-color: #ccc;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1px solid #70b231;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 808, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setText(QCoreApplication.translate("MainWindow", u"Control de H\u00e1bitos", None))
        self.lista.setText(QCoreApplication.translate("MainWindow", u"Lista de H\u00e1bitos:", None))
        self.btnagreagar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.lbnombre.setText(QCoreApplication.translate("MainWindow", u"Nombre H\u00e1bito:", None))
        self.lbdesde.setText(QCoreApplication.translate("MainWindow", u"Desde:", None))
        self.lbhasta.setText(QCoreApplication.translate("MainWindow", u"Hasta:", None))
        self.lbinicio.setText(QCoreApplication.translate("MainWindow", u"Fecha Inicio:", None))
        self.lbhasta_2.setText(QCoreApplication.translate("MainWindow", u"Fecha Hasta:", None))
        self.txtnombre.setText("")
        self.btneliminar.setText(QCoreApplication.translate("MainWindow", u"Elimininar", None))
        self.btnmostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.btneditar.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.lblclave.setText(QCoreApplication.translate("MainWindow", u"Clave:", None))
    # retranslateUi

