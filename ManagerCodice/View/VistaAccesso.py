# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\513x228.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Controller import Accesso
from View import VistaGiocatore, VistaMaster
from Model import Utente


class Ui_Login(object):

    windowList = []

    def setupUi(self, Login):
        self.gestoreAccesso = Accesso.Accesso()
        Login.setObjectName("Login")
        Login.resize(513, 228)
        Login.setMinimumSize(QtCore.QSize(513, 228))
        Login.setMaximumSize(QtCore.QSize(513, 228))
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonRegistrazione = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRegistrazione.setObjectName("buttonRegistrazione")
        self.gridLayout_3.addWidget(self.buttonRegistrazione, 4, 1, 1, 1)
        self.buttonRegistrazione.clicked.connect(self.registrazione)
        self.leNomeUtente = QtWidgets.QLineEdit(self.centralwidget)
        self.leNomeUtente.setObjectName("leNomeUtente")
        self.gridLayout_3.addWidget(self.leNomeUtente, 1, 1, 1, 1)
        self.lePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lePassword.setObjectName("lePassword")
        self.gridLayout_3.addWidget(self.lePassword, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.buttonLogin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLogin.setObjectName("buttonLogin")
        self.buttonLogin.clicked.connect(self.login)
        self.gridLayout_3.addWidget(self.buttonLogin, 5, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Registrazione"))
        self.label.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:12pt;\">Inserire nome utente e password per accedere.</span></p></body></html>"))
        self.buttonRegistrazione.setText(_translate("Login", "Registrazione"))
        self.label_2.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:12pt;\">Nome Utente:</span></p></body></html>"))
        self.label_3.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:12pt;\">Password:</span></p></body></html>"))
        self.buttonLogin.setText(_translate("Login", "Login"))

    def registrazione(self):
        if self.leNomeUtente.text() == "":
            nomeVuoto = QMessageBox()
            nomeVuoto.setWindowTitle("Errore!")
            nomeVuoto.setText("Nessun nome utente inserito")
            nomeVuoto.exec_()
            return
        valoreNomeUtente = self.leNomeUtente.text()
        if self.lePassword.text() == "":
            nomeVuoto = QMessageBox()
            nomeVuoto.setWindowTitle("Errore!")
            nomeVuoto.setText("Nessuna password inserita")
            nomeVuoto.exec_()
            return
        valorePassword = self.lePassword.text()
        nuovoUtente = self.gestoreAccesso.registrazione(valoreNomeUtente, valorePassword)
        if type(nuovoUtente) is Utente.Utente:
            windowGiocatore = QtWidgets.QWidget()
            self.windowList.append(windowGiocatore)
            self.ui = VistaGiocatore.Ui_Form()
            self.ui.setupUi(windowGiocatore, nuovoUtente)
            windowGiocatore.show()
        else:
            popup = QMessageBox()
            popup.setText("Nome utente già esistente")
            popup.setWindowTitle("Errore!")
            popup.exec_()

    def login(self):
        if self.leNomeUtente.text() == "":
            nomeVuoto = QMessageBox()
            nomeVuoto.setWindowTitle("Errore!")
            nomeVuoto.setText("Nessun nome utente inserito")
            nomeVuoto.exec_()
            return
        valoreNomeUtente = self.leNomeUtente.text()
        if self.lePassword.text() == "":
            nomeVuoto = QMessageBox()
            nomeVuoto.setWindowTitle("Errore!")
            nomeVuoto.setText("Nessuna password inserita")
            nomeVuoto.exec_()
            return
        valorePassword = self.lePassword.text()
        currentUtente = self.gestoreAccesso.login(valoreNomeUtente, valorePassword)
        if type(currentUtente) is Utente.Utente:
            if not currentUtente.isMaster:
                windowGiocatore = QtWidgets.QWidget()
                self.windowList.append(windowGiocatore)
                self.ui = VistaGiocatore.Ui_Form()
                self.ui.setupUi(windowGiocatore, currentUtente)
                windowGiocatore.show()
            else:
                windowMaster = QtWidgets.QWidget()
                self.windowList.append(windowMaster)
                self.ui = VistaMaster.Ui_Form()
                self.ui.setupUi(windowMaster, currentUtente)
                windowMaster.show()
        else:
            match currentUtente:
                case "Password":
                    popup = QMessageBox()
                    popup.setText("Password errata")
                    popup.setWindowTitle("Errore!")
                    popup.exec_()
                case "Utente":
                    popup = QMessageBox()
                    popup.setText("Nome utente non trovato")
                    popup.setWindowTitle("Errore!")
                    popup.exec_()