import os
import random, pickle, Accesso
from Model import Utilities,Utente, Appunti

class Master:

    utente = Utente.Utente()
    appunto = Appunti.Appunti()

    def __init__(self, utente, appunto):
        self.utente = utente
        self.appunto = appunto
        self.listaAppunti = []

    def cambioCredenziali(self, nomeUtente, password, id):
        self.accesso = Accesso.Accesso()
        for x in self.accesso.listaUtenti:
            if (nomeUtente == x):
                print("nome utente già esistente")
                return
        self.utente.setNomeUtente(self, nomeUtente)
        self.utente.setPassword(self, password)
        self.utente.setId(self, id)

    def creaAppunti(self, nome, immagine, informazioni):
        self.appunto.setNome(nome)
        self.appunto.setImmagine(immagine)
        self.appunto.setInformazioni(informazioni)
        self.salvaAppunti()
        self.caricaAppunti()

    def visualizzaAppunti(self, nomeAppunto):
        return self.trovaAppunti(nomeAppunto) #TODO da verificare correttezza

    def aggiornaAppunti(self,nomeAppunto, immagine, informazioni):
        if nomeAppunto == self.trovaAppunti(nomeAppunto): #TODO da verificare correttezza
            if self.appunto.getImmagine() != immagine:
                self.appunto.setImmagine(immagine)
            else:
                return "Already up-to-date"
            if self.appunto.getInformazioni() != informazioni:
                self.appunto.setInformazioni(informazioni)
            else:
                return "Already up-to-date"
            self.salvaAppunti()
            self.caricaAppunti()
            return "File not found"

    def eliminaAppunti(self, nomeAppunto):
        os.remove(self.trovaAppunti(nomeAppunto)) #TODO da verificare correttezza

    def salvaAppunti(self):
        with open("\InsiemeAppunti\\" + self.appunto.getNome(), "wb") as f: #TODo da verificare correttezza
            pickle.dump(self.appunto, f, pickle.HIGHEST_PROTOCOL)

    def caricaAppunti(self):
        if os.path.isfile(self.appunto.getNome() + ".pickle"): #TODO da verificare correttezza
            with open(self.appunto.getNome(), "rb") as f:
                self.listaAppunti = pickle.load(f)

    def trovaAppunti(self, nomeAppunto):
        self.caricaAppunti()
        for i in self.listaAppunti:
            if nomeAppunto == i.getNome():
                return self.listaAppunti[i]
        return "File not found"

    def pubblicaAppunti(self):
        #TODO
        pass

    def trovaPersonaggi(self):
        #TODO
        pass

    def aggiornaPersonaggi(self):
        #TODO
        pass

    def visualizzaPersonaggi(self):
        #TODO
        pass

    def tiraDado(self, numeroFacce, numeroLanci):
        self.dado = Utilities.Dado(numeroFacce, numeroLanci)
        return random.randint(1, self.dado.numeroFacce) * self.dado.numeroLanci

    def caricaContatore(self):
        contatore = 0
        if (os.path.exists("contatore.txt")):
            with open("contatore.txt") as fileContatore:
                contatore = fileContatore.read()
        fileContatore.close()
        self.contatoreAttuale = Utilities.Contatore(contatore)

    def incrementaContatore(self):
        self.contatoreAttuale.contatore += 1

    def resettaContatore(self):
        self.contatoreAttuale.contatore = 0

    def visualizzaContatore(self):
        if (self.contatoreAttuale.contatore < 0):
            self.resettaContatore()
        return self.contatoreAttuale.contatore

    def salvaContatore(self):
        fileContatore = open("contatore.txt", 'w')
        fileContatore.write(self.contatoreAttuale.contatore)
        fileContatore.close()

    def creaStatistiche(self):
        #TODO
        pass
