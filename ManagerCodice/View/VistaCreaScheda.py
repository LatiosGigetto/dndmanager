# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\creaScheda.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 812)
        MainWindow.setMinimumSize(QtCore.QSize(651, 812))
        MainWindow.setMaximumSize(QtCore.QSize(651, 812))
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.lineInt = QtWidgets.QLineEdit(self.centralwidget)
        self.lineInt.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineInt.setObjectName("lineInt")
        self.gridLayout.addWidget(self.lineInt, 3, 2, 1, 1)
        self.lineSagg = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSagg.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineSagg.setObjectName("lineSagg")
        self.gridLayout.addWidget(self.lineSagg, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.LineDestr = QtWidgets.QLineEdit(self.centralwidget)
        self.LineDestr.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.LineDestr.setObjectName("LineDestr")
        self.gridLayout.addWidget(self.LineDestr, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 1, 1, 1)
        self.lineCar = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCar.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineCar.setObjectName("lineCar")
        self.gridLayout.addWidget(self.lineCar, 5, 2, 1, 1)
        self.lineCost = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCost.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineCost.setObjectName("lineCost")
        self.gridLayout.addWidget(self.lineCost, 2, 2, 1, 1)
        self.lineForza = QtWidgets.QLineEdit(self.centralwidget)
        self.lineForza.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineForza.setObjectName("lineForza")
        self.gridLayout.addWidget(self.lineForza, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 5, 1, 1, 1)
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
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 6, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 7, 1, 1, 1)
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
        self.sceltaTS = QtWidgets.QComboBox(self.centralwidget)
        self.sceltaTS.setObjectName("sceltaTS")
        self.sceltaTS.addItem("")
        self.sceltaTS.addItem("")
        self.sceltaTS.addItem("")
        self.sceltaTS.addItem("")
        self.sceltaTS.addItem("")
        self.sceltaTS.addItem("")
        self.gridLayout_2.addWidget(self.sceltaTS, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 5, 0, 2, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 7, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 8, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Inserisci i parametri del personaggio:"))
        self.label_5.setText(_translate("MainWindow", "Intelligenza"))
        self.label_6.setText(_translate("MainWindow", "Saggezza"))
        self.label_4.setText(_translate("MainWindow", "Costituzione"))
        self.label_2.setText(_translate("MainWindow", "Forza"))
        self.label_3.setText(_translate("MainWindow", "Destrezza"))
        self.label_7.setText(_translate("MainWindow", "Carisma"))
        self.label_11.setText(_translate("MainWindow", "Punti Ferita"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Acrobazia"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Addestrare Animali"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Arcano"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Atletica"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Furtività"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Indagare"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Inganno"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Intimidire"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Intrattenere"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Intuizione"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Medicina"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Natura"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Percezione"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Persuasione"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Rapidità di Mano"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Religione"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Sopravvivenza"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Storia"))
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
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Acrobazia"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Addestrare Animali"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Arcano"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Atletica"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Furtività"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Indagare"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Inganno"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Intimidire"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Intrattenere"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Intuizione"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Medicina"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Natura"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Percezione"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Persuasione"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Rapidità di Mano"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "Religione"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "Sopravvivenza"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "Storia"))
        self.label_9.setText(_translate("MainWindow", "Classe"))
        self.sceltaTS.setItemText(0, _translate("MainWindow", "Forza"))
        self.sceltaTS.setItemText(1, _translate("MainWindow", "Destrezza"))
        self.sceltaTS.setItemText(2, _translate("MainWindow", "Costituzione"))
        self.sceltaTS.setItemText(3, _translate("MainWindow", "Intelligenza"))
        self.sceltaTS.setItemText(4, _translate("MainWindow", "Saggezza"))
        self.sceltaTS.setItemText(5, _translate("MainWindow", "Carisma"))
        self.label_13.setText(_translate("MainWindow", "Abilità"))
        self.label_14.setText(_translate("MainWindow", "Storia personaggio"))
        self.label_12.setText(_translate("MainWindow", "Tiri Salvezza"))
        self.pushButton.setText(_translate("MainWindow", "Conferma"))
