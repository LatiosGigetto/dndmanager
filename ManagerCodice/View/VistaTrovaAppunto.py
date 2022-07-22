import os.path

from PyQt5 import QtWidgets, QtCore

from View import VistaVisualizzaScheda, VistaModificaScheda, VistaAccesso, VistaVisualizzaAppunto, VistaModificaAppunto
from Controller import Giocatore

from Model import Appunto


class Ui_TrovaApp(object):

    def setupUi(self, Form, gestoreMaster, next):
        self.next = next
        self.gestore = gestoreMaster
        self.Form = Form
        self.leRicerca = QtWidgets.QLineEdit(Form)
        self.testoRicerca = QtWidgets.QLabel(Form)
        self.testoRicerca.setText("Inserisci il nome dell'appunto")
        self.buttonConferma = QtWidgets.QPushButton(Form)
        self.buttonConferma.setText("Cerca")
        self.buttonConferma.clicked.connect(self.trovaApp)
        self.layout = QtWidgets.QVBoxLayout(Form)
        self.layout.addWidget(self.testoRicerca)
        self.layout.addWidget(self.leRicerca)
        self.layout.addWidget(self.buttonConferma)
        self.Form.setWindowTitle("Ricerca")
        self.Form.resize(150, 150)


    def trovaApp(self):
        appunto = self.gestore.caricaAppunti(self.leRicerca.text())
        if appunto:
            match self.next:
                case "Visualizza":
                    self.ui = VistaVisualizzaAppunto.Ui_MainWindow()
                    windowVisApp = QtWidgets.QDialog()
                    VistaAccesso.Ui_Login.windowList.append(windowVisApp)
                    self.ui.setupUi(windowVisApp, self.gestore)
                    windowVisApp.show()
                case "Modifica":
                    self.ui = VistaModificaAppunto.Ui_CreaApp()
                    windowModApp = QtWidgets.QDialog()
                    VistaAccesso.Ui_Login.windowList.append(windowModApp)
                    self.ui.setupUi(windowModApp, self.gestore)
                    windowModApp.show()
                case "Elimina":
                    if os.path.isfile("Appunti/" + self.gestore.appunto.getNome() + ".pickle"):
                        os.remove("Appunti/" + self.gestore.appunto.getNome() + ".pickle")
                        if os.path.isfile("Appunti/" + self.gestore.appunto.getNome() + ".jpg"):
                            os.remove("Appunti/" + self.gestore.appunto.getNome() + ".jpg")
                        self.gestore.appunto = Appunto.Appunto()
                        popup = QtWidgets.QMessageBox()
                        popup.setText("Appunto eliminato")
                        popup.setWindowTitle("Successo")
                        popup.exec_()
                case "Pubblica":
                    if os.path.isfile("Appunti/" + self.gestore.appunto.getNome() + ".pickle"):
                        if self.gestore.appunto.getIspublic():
                            popup = QtWidgets.QMessageBox()
                            popup.setText("Appunto già pubblico")
                            popup.setWindowTitle("Errore")
                            popup.exec_()
                            return
                        self.gestore.pubblicaAppunti(self.gestore.appunto.getNome())
                        popup = QtWidgets.QMessageBox()
                        popup.setText("Appunto pubblicato")
                        popup.setWindowTitle("Successo")
                        popup.exec_()
                        return
                case "Dispense":
                    if not self.gestore.appunto.getIspublic():
                        popup = QtWidgets.QMessageBox()
                        popup.setText("Appunto non pubblico")
                        popup.setWindowTitle("Errore")
                        popup.exec_()
                        return
                    self.ui = VistaVisualizzaAppunto.Ui_MainWindow()
                    windowVisApp = QtWidgets.QDialog()
                    VistaAccesso.Ui_Login.windowList.append(windowVisApp)
                    self.ui.setupUi(windowVisApp, self.gestore)
                    windowVisApp.show()
            self.Form.close()
        else:
            popup = QtWidgets.QMessageBox()
            popup.setText("Appunto non trovato")
            popup.setWindowTitle("Errore")
            popup.exec_()
            return

