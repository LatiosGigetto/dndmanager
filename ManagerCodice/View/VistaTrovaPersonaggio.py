from PyQt5 import QtWidgets

from Controller import Accesso, Master


class Ui_TrovaPG(object):
    def setupUi(self, Form):
        self.Form = Form
        self.leRicerca = QtWidgets.QLineEdit(Form)
        self.testoRicerca = QtWidgets.QLabel(Form)
        self.testoRicerca.setText("Inserisci il nome dell'utente")
        self.buttonConferma = QtWidgets.QPushButton(Form)
        self.buttonConferma.setText("Cerca")
        self.layout = QtWidgets.QVBoxLayout(Form)
        self.layout.addWidget(self.testoRicerca)
        self.layout.addWidget(self.leRicerca)
        self.layout.addWidget(self.buttonConferma)
        self.Form.setWindowTitle("Ricerca")
        self.Form.resize(150, 150)


    def trovaPG(self):
        utente = self.testoRicerca.text()
        Master.Master.trovaPersonaggi()
