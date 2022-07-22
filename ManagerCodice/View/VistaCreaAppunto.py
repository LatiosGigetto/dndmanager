import os.path

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIntValidator


class Ui_CreaApp(object):

    def setupUi(self, Form, gestore):
        self.Form = Form
        self.gestore = gestore
        self.immagine = ()
        self.isNPC = False
        self.Form.resize(600, 600)
        self.Form.setWindowTitle("Crea Appunto")
        self.layout = QtWidgets.QGridLayout(Form)
        self.labelNome = QtWidgets.QLabel(Form)
        self.labelNome.setText("Nome appunto")
        self.layout.addWidget(self.labelNome, 0, 0)
        self.leNome = QtWidgets.QLineEdit(Form)
        self.layout.addWidget(self.leNome, 0, 1)
        self.labelTesto = QtWidgets.QLabel(Form)
        self.labelTesto.setText("Testo appunto")
        self.layout.addWidget(self.labelTesto, 1, 0)
        self.textAppunto = QtWidgets.QTextEdit(Form)
        self.layout.addWidget(self.textAppunto, 1, 1)
        self.buttonCarica = QtWidgets.QPushButton(Form)
        self.buttonCarica.setText("Carica immagine")
        self.layout.addWidget(self.buttonCarica, 2, 0)
        self.buttonCarica.clicked.connect(self.carica)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setText("NPC")
        self.layout.addWidget(self.checkBox, 2, 1)
        self.checkBox.clicked.connect(self.NPC)
        self.labelSfida = QtWidgets.QLabel(Form)
        self.labelSfida.setText("Grado sfida:")
        self.layout.addWidget(self.labelSfida, 3, 0)
        self.leSfida = QtWidgets.QLineEdit(Form)
        self.leSfida.setDisabled(True)
        self.layout.addWidget(self.leSfida, 3, 1)
        self.buttonCrea = QtWidgets.QPushButton(Form)
        self.buttonCrea.setText("Conferma")
        self.layout.addWidget(self.buttonCrea, 4, 0)
        self.buttonCrea.clicked.connect(self.crea)

        self.validator = QIntValidator(0, 30)
        self.leSfida.setValidator(self.validator)


    def carica(self):
        self.immagine = QtWidgets.QFileDialog.getOpenFileName(self.Form, "Scegli immagine", filter="Images (*.png *.xpm *.jpg)")


    def NPC(self):
        if self.checkBox.isChecked():
            self.isNPC = True
            self.leSfida.setDisabled(False)
        else:
            self.isNPC = False
            self.leSfida.setDisabled(True)

    def crea(self):
        if not (self.leNome.text() and self.textAppunto.toPlainText()):
            popup = QtWidgets.QMessageBox()
            popup.setText("Inserisci tutti i parametri")
            popup.setWindowTitle("Errore")
            popup.exec_()
            return

        if self.isNPC and not self.leSfida.text():
            popup = QtWidgets.QMessageBox()
            popup.setText("Inserisci tutti i parametri")
            popup.setWindowTitle("Errore")
            popup.exec_()
            return

        if os.path.isfile("Appunti/" + self.leNome.text() + ".pickle"):
            popup = QtWidgets.QMessageBox()
            popup.setText("Appunto già esistente con quel nome")
            popup.setWindowTitle("Errore")
            popup.exec_()
            return

        if self.immagine:
            self.gestore.creaAppunti(self.leNome.text(), nomeImmagine=self.immagine[0], informazioni=self.textAppunto.toPlainText(), isNPC=self.isNPC,
                                     gradoSfida=self.leSfida.text())
        else:
            self.gestore.creaAppunti(self.leNome.text(), informazioni=self.textAppunto.toPlainText(), isNPC=self.isNPC, gradoSfida=self.leSfida.text())

        popup = QtWidgets.QMessageBox()
        popup.setText("Appunto creato con successo")
        popup.setWindowTitle("DnD Manager")
        popup.exec_()
        self.Form.close()
