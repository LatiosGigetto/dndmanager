# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MenuGiocatore.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Controller import Giocatore
from View import VistaCreaScheda, VistaAccesso
from Model import Utente

class Ui_Form(object):
    def setupUi(self, Form, currentUtente:Utente.Utente):
        self.gestoreGiocatore = Giocatore.Giocatore(currentUtente)
        Form.setObjectName("DnD Manager")
        Form.resize(566, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 1, 1, 1)
        self.buttonCreaScheda = QtWidgets.QPushButton(Form)
        self.buttonCreaScheda.setObjectName("buttonCreaScheda")
        self.gridLayout.addWidget(self.buttonCreaScheda, 1, 0, 1, 1)
        self.buttonCreaScheda.clicked.connect(self.goCreaScheda)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.goCreaScheda()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DnD Manager"))
        self.label.setText(_translate("Form", ("<html><head/><body><p><span style=\" font-size:14pt;\">Id:" + self.gestoreGiocatore.utente.id + "</span></p><p><span style=\" font-size:14pt;\">Ruolo: Giocatore</span></p><p><span style=\" font-size:14pt;\">Utente: " + self.gestoreGiocatore.utente.getNomeUtente() + "</span></p><p><br/></p></body></html>")))
        self.pushButton_7.setText(_translate("Form", "Cambia Credenziali"))
        self.buttonCreaScheda.setText(_translate("Form", "Crea Scheda"))
        self.pushButton.setText(_translate("Form", "Visualizza Scheda"))
        self.pushButton_3.setText(_translate("Form", "Modifica Scheda"))
        self.pushButton_6.setText(_translate("Form", "Visualizza Dispense"))
        self.pushButton_4.setText(_translate("Form", "Tira i dadi"))
        self.pushButton_5.setText(_translate("Form", "Note"))


    def goCreaScheda(self):
        print("zioperone")
        #if self.gestoreGiocatore.utente.personaggio.getNome:
            #print("pallone")
            #popup = QtWidgets.QMessageBox()
            #popup.setText("Personaggio già esisente")
            #popup.setWindowTitle("Errore")
            #popup.exec_()
        print("ziopera")
        ui = VistaCreaScheda.Ui_MainWindow()
        windowCreaScheda = QtWidgets.QMainWindow()
        VistaAccesso.Ui_Login.windowList.append(windowCreaScheda)
        ui.setupUi(windowCreaScheda, self.gestoreGiocatore)
        print("culone")
        windowCreaScheda.show()
        return True





