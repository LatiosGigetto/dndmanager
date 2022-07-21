from PyQt5 import QtCore, QtWidgets, QtGui
from Controller import Giocatore

class Ui_Scheda(object):

    def setupUi(self, Dialog, gestoreGiocatore:Giocatore.Giocatore):
        self.gestoreGiocatore = gestoreGiocatore
        Dialog.resize(651, 612)
        Dialog.setMinimumSize(QtCore.QSize(651, 612))
        Dialog.setMaximumSize(QtCore.QSize(651, 612))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.labelSag = QtWidgets.QLabel(Dialog)
        self.labelSag.setText("Saggezza")
        self.gridLayout.addWidget(self.labelSag, 5, 0, 1, 1)
        self.labelInt = QtWidgets.QLabel(Dialog)
        self.labelInt.setText("Intelligenza")
        self.gridLayout.addWidget(self.labelInt, 4, 0, 1, 1)
        self.textSagg = QtWidgets.QLabel(Dialog)
        self.textSagg.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.gridLayout.addWidget(self.textSagg, 5, 1, 1, 1)
        self.textInt = QtWidgets.QLabel(Dialog)
        self.textInt.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textInt.setObjectName("textInt")
        self.gridLayout.addWidget(self.textInt, 4, 1, 1, 1)
        self.labelCon = QtWidgets.QLabel(Dialog)
        self.labelCon.setText("Costituzione")
        self.gridLayout.addWidget(self.labelCon, 3, 0, 1, 1)
        self.textDestr = QtWidgets.QLabel(Dialog)
        self.textDestr.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textDestr.setObjectName("textDestr")
        self.gridLayout.addWidget(self.textDestr, 2, 1, 1, 1)
        self.labelCar = QtWidgets.QLabel(Dialog)
        self.labelCar.setText("Carisma")
        self.gridLayout.addWidget(self.labelCar, 6, 0, 1, 1)
        self.labelForza = QtWidgets.QLabel(Dialog)
        self.labelForza.setText("Forza")
        self.gridLayout.addWidget(self.labelForza, 1, 0, 1, 1)
        self.labelDestrezza = QtWidgets.QLabel(Dialog)
        self.labelDestrezza.setText("Destrezza")
        self.gridLayout.addWidget(self.labelDestrezza, 2, 0, 1, 1)
        self.textCar = QtWidgets.QLabel(Dialog)
        self.textCar.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textCar.setObjectName("textCar")
        self.gridLayout.addWidget(self.textCar, 6, 1, 1, 1)
        self.textCost = QtWidgets.QLabel(Dialog)
        self.textCost.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textCost.setObjectName("textCost")
        self.gridLayout.addWidget(self.textCost, 3, 1, 1, 1)
        self.textForza = QtWidgets.QLabel(Dialog)
        self.textForza.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textForza.setObjectName("textForza")
        self.gridLayout.addWidget(self.textForza, 1, 1, 1, 1)
        self.labelNome = QtWidgets.QLabel(Dialog)
        self.labelNome.setText("Nome")
        self.gridLayout.addWidget(self.labelNome, 0, 0, 1, 1)
        self.textNome = QtWidgets.QLabel(Dialog)
        self.textNome.setObjectName("textNome")
        self.gridLayout.addWidget(self.textNome, 0, 1, 1, 1)
        self.labelCA = QtWidgets.QLabel(Dialog)
        self.labelCA.setText("Classe Armatura")
        self.gridLayout.addWidget(self.labelCA, 10, 0, 1, 1)
        self.textAbi1 = QtWidgets.QLabel(Dialog)
        self.textAbi1.setObjectName("textAbi1")
        self.gridLayout.addWidget(self.textAbi1, 13, 1, 1, 1)
        self.labelClasse = QtWidgets.QLabel(Dialog)
        self.labelClasse.setText("Classe")
        self.gridLayout.addWidget(self.labelClasse, 7, 0, 1, 1)
        self.textLivello = QtWidgets.QLabel(Dialog)
        self.textLivello.setObjectName("textLivello")
        self.gridLayout.addWidget(self.textLivello, 8, 1, 1, 1)
        self.labelPF = QtWidgets.QLabel(Dialog)
        self.labelPF.setText("Punti Ferita")
        self.gridLayout.addWidget(self.labelPF, 9, 0, 1, 1)
        self.textClasse = QtWidgets.QLabel(Dialog)
        self.textClasse.setObjectName("textClasse")
        self.gridLayout.addWidget(self.textClasse, 7, 1, 1, 1)
        self.textAbi2 = QtWidgets.QLabel(Dialog)
        self.textAbi2.setObjectName("textAbi2")
        self.gridLayout.addWidget(self.textAbi2, 14, 1, 1, 1)
        self.textStoria = QtWidgets.QLabel(Dialog)
        self.textStoria.setObjectName("textStoria")
        self.gridLayout.addWidget(self.textStoria, 15, 1, 1, 1)
        self.textPF = QtWidgets.QLabel(Dialog)
        self.textPF.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textPF.setObjectName("textPF")
        self.gridLayout.addWidget(self.textPF, 9, 1, 1, 1)
        self.labelLivello = QtWidgets.QLabel(Dialog)
        self.labelLivello.setText("Livello")
        self.gridLayout.addWidget(self.labelLivello, 8, 0, 1, 1)
        self.textCA = QtWidgets.QLabel(Dialog)
        self.textCA.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textCA.setObjectName("lineCA")
        self.gridLayout.addWidget(self.textCA, 10, 1, 1, 1)
        #self.textTS1 = QtWidgets.QLabel(Dialog)                Non implementato
        #self.textTS1.setObjectName("sceltaTS1")
        #self.gridLayout.addWidget(self.textTS1, 11, 1, 1, 1)
        #self.textTS2 = QtWidgets.QLabel(Dialog)
        #self.textTS2.setObjectName("sceltaTS2")
        #self.gridLayout.addWidget(self.textTS2, 12, 1, 1, 1)
        #self.labelAbi = QtWidgets.QLabel(Dialog)
        #self.labelAbi.setText("Abilità")
        #self.gridLayout.addWidget(self.labelAbi, 13, 0, 2, 1)
        #self.labelStoria = QtWidgets.QLabel(Dialog)
        #self.labelStoria.setText("Storia personaggio")
        #self.gridLayout.addWidget(self.labelStoria, 15, 0, 1, 1)
        #self.labelTS = QtWidgets.QLabel(Dialog)
        #self.labelTS.setText("Tiri Salvezza")
        #self.gridLayout.addWidget(self.labelTS, 11, 0, 1, 1)

        self.visualizza()

    def visualizza(self):
        personaggio = self.gestoreGiocatore.visualizzaScheda()
        self.textNome.setText(personaggio.nome)
        self.textForza.setText(str(personaggio.punteggi['Forza']))
        self.textDestr.setText(str(personaggio.punteggi["Destrezza"]))
        self.textCost.setText(str(personaggio.punteggi["Costituzione"]))
        self.textInt.setText(str(personaggio.punteggi["Intelligenza"]))
        self.textSagg.setText(str(personaggio.punteggi["Saggezza"]))
        self.textCar.setText(str(personaggio.punteggi["Carisma"]))
        self.textClasse.setText(personaggio.classe)
        self.textLivello.setText(str(personaggio.livello))
        self.textCA.setText(str(personaggio.armatura))
        self.textPF.setText(str(personaggio.puntiFerita))
        #self.textTS1.setText(personaggio.nome)     Non implementato
        #self.textTS2.setText(personaggio.nome)
        #self.textAbi1.setText(personaggio.nome)
        #self.textAbi2.setText(personaggio.nome)
        #self.textStoria.setText(personaggio.storia)