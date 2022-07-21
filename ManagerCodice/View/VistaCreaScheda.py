# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\creaScheda.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os.path

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator

from Controller import Giocatore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, gestoreGiocatore):
        self.gestoreGiocatore = gestoreGiocatore
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setWindowTitle("Crezione Scheda")
        self.MainWindow.resize(651, 812)
        self.MainWindow.setMinimumSize(QtCore.QSize(651, 812))
        self.MainWindow.setMaximumSize(QtCore.QSize(651, 812))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelSag = QtWidgets.QLabel(self.centralwidget)
        self.labelSag.setObjectName("labelSag")
        self.gridLayout.addWidget(self.labelSag, 5, 1, 1, 1)
        self.labelInt = QtWidgets.QLabel(self.centralwidget)
        self.labelInt.setObjectName("labelInt")
        self.gridLayout.addWidget(self.labelInt, 4, 1, 1, 1)
        self.lineSagg = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSagg.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineSagg.setObjectName("lineSagg")
        self.gridLayout.addWidget(self.lineSagg, 5, 2, 1, 1)
        self.lineInt = QtWidgets.QLineEdit(self.centralwidget)
        self.lineInt.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineInt.setObjectName("lineInt")
        self.gridLayout.addWidget(self.lineInt, 4, 2, 1, 1)
        self.labelCon = QtWidgets.QLabel(self.centralwidget)
        self.labelCon.setObjectName("labelCon")
        self.gridLayout.addWidget(self.labelCon, 3, 1, 1, 1)
        self.lineDestr = QtWidgets.QLineEdit(self.centralwidget)
        self.lineDestr.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineDestr.setObjectName("LineDestr")
        self.gridLayout.addWidget(self.lineDestr, 2, 2, 1, 1)
        self.labelCar = QtWidgets.QLabel(self.centralwidget)
        self.labelCar.setObjectName("labelCar")
        self.gridLayout.addWidget(self.labelCar, 6, 1, 1, 1)
        self.labelForza = QtWidgets.QLabel(self.centralwidget)
        self.labelForza.setObjectName("labelForza")
        self.gridLayout.addWidget(self.labelForza, 1, 1, 1, 1)
        self.labelDestrezza = QtWidgets.QLabel(self.centralwidget)
        self.labelDestrezza.setObjectName("labelDestrezza")
        self.gridLayout.addWidget(self.labelDestrezza, 2, 1, 1, 1)
        self.lineCar = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCar.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineCar.setObjectName("lineCar")
        self.gridLayout.addWidget(self.lineCar, 6, 2, 1, 1)
        self.lineCost = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCost.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineCost.setObjectName("lineCost")
        self.gridLayout.addWidget(self.lineCost, 3, 2, 1, 1)
        self.lineForza = QtWidgets.QLineEdit(self.centralwidget)
        self.lineForza.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineForza.setObjectName("lineForza")
        self.gridLayout.addWidget(self.lineForza, 1, 2, 1, 1)
        self.labelNome = QtWidgets.QLabel(self.centralwidget)
        self.labelNome.setObjectName("labelNome")
        self.gridLayout.addWidget(self.labelNome, 0, 1, 1, 1)
        self.lineNome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineNome.setObjectName("lineNome")
        self.gridLayout.addWidget(self.lineNome, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.sceltaAbi1 = QtWidgets.QComboBox(self.centralwidget)
        self.sceltaAbi1.setObjectName("sceltaAbi1")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.sceltaAbi1.addItem("")
        self.gridLayout_2.addWidget(self.sceltaAbi1, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.sceltaLivello = QtWidgets.QComboBox(self.centralwidget)
        self.sceltaLivello.setObjectName("sceltaLivello")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.sceltaLivello.addItem("")
        self.gridLayout_2.addWidget(self.sceltaLivello, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.sceltaClasse = QtWidgets.QComboBox(self.centralwidget)
        self.sceltaClasse.setObjectName("sceltaClasse")
        self.sceltaClasse.addItem("")
        self.sceltaClasse.addItem("")
        self.sceltaClasse.addItem("")
        self.sceltaClasse.addItem("")
        self.sceltaClasse.addItem("")
        self.sceltaClasse.addItem("")
        self.sceltaClasse.addItem("")
        self.sceltaClasse.addItem("")
        self.sceltaClasse.addItem("")
        self.sceltaClasse.addItem("")
        self.sceltaClasse.addItem("")
        self.sceltaClasse.addItem("")
        self.gridLayout_2.addWidget(self.sceltaClasse, 0, 1, 1, 1)
        self.sceltaAbi2 = QtWidgets.QComboBox(self.centralwidget)
        self.sceltaAbi2.setObjectName("sceltaAbi2")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.sceltaAbi2.addItem("")
        self.gridLayout_2.addWidget(self.sceltaAbi2, 7, 1, 1, 1)
        self.textEditStoria = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditStoria.setObjectName("textEditStoria")
        self.gridLayout_2.addWidget(self.textEditStoria, 8, 1, 1, 1)
        self.linePF = QtWidgets.QLineEdit(self.centralwidget)
        self.linePF.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.linePF.setObjectName("linePF")
        self.gridLayout_2.addWidget(self.linePF, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineCA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCA.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineCA.setObjectName("lineCA")
        self.gridLayout_2.addWidget(self.lineCA, 3, 1, 1, 1)
        self.sceltaTS1 = QtWidgets.QComboBox(self.centralwidget)
        self.sceltaTS1.setObjectName("sceltaTS1")
        self.sceltaTS1.addItem("")
        self.sceltaTS1.addItem("")
        self.sceltaTS1.addItem("")
        self.sceltaTS1.addItem("")
        self.sceltaTS1.addItem("")
        self.sceltaTS1.addItem("")
        self.gridLayout_2.addWidget(self.sceltaTS1, 4, 1, 1, 1)

        self.sceltaTS2 = QtWidgets.QComboBox(self.centralwidget)
        self.sceltaTS2.setObjectName("sceltaTS2")
        self.sceltaTS2.addItem("")
        self.sceltaTS2.addItem("")
        self.sceltaTS2.addItem("")
        self.sceltaTS2.addItem("")
        self.sceltaTS2.addItem("")
        self.sceltaTS2.addItem("")
        self.gridLayout_2.addWidget(self.sceltaTS2, 5, 1, 1, 1)

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 6, 0, 2, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 8, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)
        self.buttonConferma = QtWidgets.QPushButton(self.centralwidget)
        self.buttonConferma.setObjectName("buttonConferma")
        self.gridLayout_2.addWidget(self.buttonConferma, 9, 0, 1, 1)
        self.buttonConferma.clicked.connect(self.creaScheda)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        punteggiValidator = QIntValidator(1, 20)
        otherValidator = QIntValidator(1, 999)
        self.lineForza.setValidator(punteggiValidator)
        self.lineDestr.setValidator(punteggiValidator)
        self.lineCost.setValidator(punteggiValidator)
        self.lineInt.setValidator(punteggiValidator)
        self.lineSagg.setValidator(punteggiValidator)
        self.lineCar.setValidator(punteggiValidator)
        self.lineCA.setValidator(otherValidator)
        self.linePF.setValidator(otherValidator)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Creazione Scheda"))
        self.label.setText(_translate("MainWindow", "Inserisci i parametri del personaggio:"))
        self.labelSag.setText(_translate("MainWindow", "Saggezza"))
        self.labelInt.setText(_translate("MainWindow", "Intelligenza"))
        self.labelCon.setText(_translate("MainWindow", "Costituzione"))
        self.labelCar.setText(_translate("MainWindow", "Carisma"))
        self.labelForza.setText(_translate("MainWindow", "Forza"))
        self.labelDestrezza.setText(_translate("MainWindow", "Destrezza"))
        self.labelNome.setText(_translate("MainWindow", "Nome"))
        self.label_11.setText(_translate("MainWindow", "Punti Ferita"))
        self.sceltaAbi1.setItemText(0, _translate("MainWindow", "Acrobazia"))
        self.sceltaAbi1.setItemText(1, _translate("MainWindow", "Addestrare Animali"))
        self.sceltaAbi1.setItemText(2, _translate("MainWindow", "Arcano"))
        self.sceltaAbi1.setItemText(3, _translate("MainWindow", "Atletica"))
        self.sceltaAbi1.setItemText(4, _translate("MainWindow", "Furtività"))
        self.sceltaAbi1.setItemText(5, _translate("MainWindow", "Indagare"))
        self.sceltaAbi1.setItemText(6, _translate("MainWindow", "Inganno"))
        self.sceltaAbi1.setItemText(7, _translate("MainWindow", "Intimidire"))
        self.sceltaAbi1.setItemText(8, _translate("MainWindow", "Intrattenere"))
        self.sceltaAbi1.setItemText(9, _translate("MainWindow", "Intuizione"))
        self.sceltaAbi1.setItemText(10, _translate("MainWindow", "Medicina"))
        self.sceltaAbi1.setItemText(11, _translate("MainWindow", "Natura"))
        self.sceltaAbi1.setItemText(12, _translate("MainWindow", "Percezione"))
        self.sceltaAbi1.setItemText(13, _translate("MainWindow", "Persuasione"))
        self.sceltaAbi1.setItemText(14, _translate("MainWindow", "Rapidità di Mano"))
        self.sceltaAbi1.setItemText(15, _translate("MainWindow", "Religione"))
        self.sceltaAbi1.setItemText(16, _translate("MainWindow", "Sopravvivenza"))
        self.sceltaAbi1.setItemText(17, _translate("MainWindow", "Storia"))
        self.label_8.setText(_translate("MainWindow", "Classe Armatura"))
        self.sceltaLivello.setItemText(0, _translate("MainWindow", "1"))
        self.sceltaLivello.setItemText(1, _translate("MainWindow", "2"))
        self.sceltaLivello.setItemText(2, _translate("MainWindow", "3"))
        self.sceltaLivello.setItemText(3, _translate("MainWindow", "4"))
        self.sceltaLivello.setItemText(4, _translate("MainWindow", "5"))
        self.sceltaLivello.setItemText(5, _translate("MainWindow", "6"))
        self.sceltaLivello.setItemText(6, _translate("MainWindow", "7"))
        self.sceltaLivello.setItemText(7, _translate("MainWindow", "8"))
        self.sceltaLivello.setItemText(8, _translate("MainWindow", "9"))
        self.sceltaLivello.setItemText(9, _translate("MainWindow", "10"))
        self.sceltaLivello.setItemText(10, _translate("MainWindow", "11"))
        self.sceltaLivello.setItemText(11, _translate("MainWindow", "12"))
        self.sceltaLivello.setItemText(12, _translate("MainWindow", "13"))
        self.sceltaLivello.setItemText(13, _translate("MainWindow", "14"))
        self.sceltaLivello.setItemText(14, _translate("MainWindow", "15"))
        self.sceltaLivello.setItemText(15, _translate("MainWindow", "16"))
        self.sceltaLivello.setItemText(16, _translate("MainWindow", "17"))
        self.sceltaLivello.setItemText(17, _translate("MainWindow", "18"))
        self.sceltaLivello.setItemText(18, _translate("MainWindow", "19"))
        self.sceltaLivello.setItemText(19, _translate("MainWindow", "20"))
        self.label_10.setText(_translate("MainWindow", "Livello"))
        self.sceltaClasse.setItemText(0, _translate("MainWindow", "Barbaro"))
        self.sceltaClasse.setItemText(1, _translate("MainWindow", "Bardo"))
        self.sceltaClasse.setItemText(2, _translate("MainWindow", "Chierico"))
        self.sceltaClasse.setItemText(3, _translate("MainWindow", "Druido"))
        self.sceltaClasse.setItemText(4, _translate("MainWindow", "Guerriero"))
        self.sceltaClasse.setItemText(5, _translate("MainWindow", "Ladro"))
        self.sceltaClasse.setItemText(6, _translate("MainWindow", "Mago"))
        self.sceltaClasse.setItemText(7, _translate("MainWindow", "Monaco"))
        self.sceltaClasse.setItemText(8, _translate("MainWindow", "Paladino"))
        self.sceltaClasse.setItemText(9, _translate("MainWindow", "Ranger"))
        self.sceltaClasse.setItemText(10, _translate("MainWindow", "Stregone"))
        self.sceltaClasse.setItemText(11, _translate("MainWindow", "Warlock"))
        self.sceltaAbi2.setItemText(0, _translate("MainWindow", "Acrobazia"))
        self.sceltaAbi2.setItemText(1, _translate("MainWindow", "Addestrare Animali"))
        self.sceltaAbi2.setItemText(2, _translate("MainWindow", "Arcano"))
        self.sceltaAbi2.setItemText(3, _translate("MainWindow", "Atletica"))
        self.sceltaAbi2.setItemText(4, _translate("MainWindow", "Furtività"))
        self.sceltaAbi2.setItemText(5, _translate("MainWindow", "Indagare"))
        self.sceltaAbi2.setItemText(6, _translate("MainWindow", "Inganno"))
        self.sceltaAbi2.setItemText(7, _translate("MainWindow", "Intimidire"))
        self.sceltaAbi2.setItemText(8, _translate("MainWindow", "Intrattenere"))
        self.sceltaAbi2.setItemText(9, _translate("MainWindow", "Intuizione"))
        self.sceltaAbi2.setItemText(10, _translate("MainWindow", "Medicina"))
        self.sceltaAbi2.setItemText(11, _translate("MainWindow", "Natura"))
        self.sceltaAbi2.setItemText(12, _translate("MainWindow", "Percezione"))
        self.sceltaAbi2.setItemText(13, _translate("MainWindow", "Persuasione"))
        self.sceltaAbi2.setItemText(14, _translate("MainWindow", "Rapidità di Mano"))
        self.sceltaAbi2.setItemText(15, _translate("MainWindow", "Religione"))
        self.sceltaAbi2.setItemText(16, _translate("MainWindow", "Sopravvivenza"))
        self.sceltaAbi2.setItemText(17, _translate("MainWindow", "Storia"))
        self.label_9.setText(_translate("MainWindow", "Classe"))
        self.sceltaTS1.setItemText(0, _translate("MainWindow", "Forza"))
        self.sceltaTS1.setItemText(1, _translate("MainWindow", "Destrezza"))
        self.sceltaTS1.setItemText(2, _translate("MainWindow", "Costituzione"))
        self.sceltaTS1.setItemText(3, _translate("MainWindow", "Intelligenza"))
        self.sceltaTS1.setItemText(4, _translate("MainWindow", "Saggezza"))
        self.sceltaTS1.setItemText(5, _translate("MainWindow", "Carisma"))
        self.sceltaTS2.setItemText(0, _translate("MainWindow", "Forza"))
        self.sceltaTS2.setItemText(1, _translate("MainWindow", "Destrezza"))
        self.sceltaTS2.setItemText(2, _translate("MainWindow", "Costituzione"))
        self.sceltaTS2.setItemText(3, _translate("MainWindow", "Intelligenza"))
        self.sceltaTS2.setItemText(4, _translate("MainWindow", "Saggezza"))
        self.sceltaTS2.setItemText(5, _translate("MainWindow", "Carisma"))
        self.label_13.setText(_translate("MainWindow", "Abilità"))
        self.label_14.setText(_translate("MainWindow", "Storia personaggio"))
        self.label_12.setText(_translate("MainWindow", "Tiri Salvezza"))
        self.buttonConferma.setText(_translate("MainWindow", "Conferma"))

    def creaScheda(self):
        punteggi = {}
        print("culone")
        if not (self.lineNome.text() and self.lineCA.text() and self.linePF.text() and self.lineForza.text() and self.lineDestr.text() \
                and self.lineCost.text() and self.lineInt.text() and self.lineSagg.text() and self.lineCar.text()):
            popup = QtWidgets.QMessageBox()
            popup.setText("Inserisci tutti i parametri")
            popup.setWindowTitle("Errore")
            popup.exec_()
            return
        if self.sceltaAbi1.currentText() == self.sceltaAbi2.currentText():
            popup = QtWidgets.QMessageBox()
            popup.setText("Scegli due abilità differenti")
            popup.setWindowTitle("Errore")
            popup.exec_()
            return
        if self.sceltaTS1.currentText() == self.sceltaTS2.currentText():
            popup = QtWidgets.QMessageBox()
            popup.setText("Scegli due tiri salvezza diversi")
            popup.setWindowTitle("Errore")
            popup.exec_()
            return

        if (len(self.lineCA.text()) or len(self.linePF.text()) or len(self.lineNome.text())) > 30 \
            or not (self.lineForza.hasAcceptableInput() and self.lineDestr.hasAcceptableInput() and self.lineCost.hasAcceptableInput()
            and self.lineInt.hasAcceptableInput() and self.lineSagg.hasAcceptableInput() and self.lineCar.hasAcceptableInput()
            and self.linePF.hasAcceptableInput() and self.lineCA.hasAcceptableInput()):

            popup = QtWidgets.QMessageBox()
            popup.setText("Inserisci parametri validi")
            popup.setWindowTitle("Errore")
            popup.exec_()
            return

        if os.path.isfile("Schede/" + self.lineNome.text() + ".pickle"):
            popup = QtWidgets.QMessageBox()
            popup.setText("Nome del personaggio già scelto")
            popup.setWindowTitle("Errore")
            popup.exec_()
            return

        punteggi = {
                "Forza": int(self.lineForza.text()),
                "Destrezza": int(self.lineDestr.text()),
                "Costituzione": int(self.lineCost.text()),
                "Intelligenza": int(self.lineInt.text()),
                "Saggezza": int(self.lineSagg.text()),
                "Carisma": int(self.lineCar.text())
            }
        self.gestoreGiocatore.creaScheda(self.lineNome.text(), punteggi, self.sceltaClasse.currentText(),
                                            int(self.sceltaLivello.currentText()), int(self.linePF.text()),
                                            int(self.lineCA.text()), self.sceltaTS1.currentText(),
                                            self.sceltaTS2.currentText(), self.sceltaAbi1.currentText(),
                                            self.sceltaAbi2.currentText(), self.textEditStoria.toPlainText())
        popup = QtWidgets.QMessageBox()
        popup.setText("Scheda creata con successo")
        popup.setWindowTitle("DnD Manager")
        popup.exec_()
        self.MainWindow.close()



