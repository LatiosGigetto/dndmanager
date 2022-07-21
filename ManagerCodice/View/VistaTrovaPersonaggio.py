from PyQt5 import QtWidgets, QtCore

from View import VistaVisualizzaScheda, VistaModificaScheda, VistaAccesso
from Controller import Giocatore


class Ui_TrovaPG(object):

    def setupUi(self, Form, gestoreMaster, next):
        self.next = next
        self.gestore = gestoreMaster
        self.Form = Form
        self.leRicerca = QtWidgets.QLineEdit(Form)
        self.testoRicerca = QtWidgets.QLabel(Form)
        self.testoRicerca.setText("Inserisci il nome dell'utente")
        self.buttonConferma = QtWidgets.QPushButton(Form)
        self.buttonConferma.setText("Cerca")
        self.buttonConferma.clicked.connect(self.trovaPG)
        self.layout = QtWidgets.QVBoxLayout(Form)
        self.layout.addWidget(self.testoRicerca)
        self.layout.addWidget(self.leRicerca)
        self.layout.addWidget(self.buttonConferma)
        self.Form.setWindowTitle("Ricerca")
        self.Form.resize(150, 150)


    def trovaPG(self):
        user = self.gestore.trovaPersonaggi(self.leRicerca.text())
        if user:
            match self.next:
                case "Visualizza":
                    self.ui = VistaVisualizzaScheda.Ui_Scheda()
                    windowVisScheda = QtWidgets.QDialog()
                    VistaAccesso.Ui_Login.windowList.append(windowVisScheda)
                    self.ui.setupUi(windowVisScheda, Giocatore.Giocatore(user))
                    windowVisScheda.show()
                case "Modifica":
                    self.ui = VistaModificaScheda.Ui_MainWindow()
                    windowModScheda = QtWidgets.QMainWindow()
                    VistaAccesso.Ui_Login.windowList.append(windowModScheda)
                    self.ui.setupUi(windowModScheda, Giocatore.Giocatore(user))
                    windowModScheda.show()
            self.Form.close()
        else:
            popup = QtWidgets.QMessageBox()
            popup.setText("Personaggio non trovato")
            popup.setWindowTitle("Errore")
            popup.exec_()
            return

