import os
import random, pickle, Accesso
from Model import Utilities,Utente

class Master:

    utente = Utente.Utente()  # creazione dell'oggetto ridondante perché è il costruttore che lo farà poi (parte da rivedere)
    def __init__(self, utente):
        self.utente = utente
    # TODO Python merda

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
        self.utente.appunto.setNome(nome)
        self.utente.appunto.setImmagine(immagine)
        self.utente.appunto.setInformazioni(informazioni)
        self.salvaAppunti()

    def aggiornaAppunti(self, immagine, informazioni):
        #TODO controllare il funzionamento
        if (self.utente.appunto.getImmagine() != immagine):
            self.utente.appunti.setImmagine(immagine)
        else:
            return "Already up-to ì-date"
        if (self.utente.appunto.getInformazioni() != informazioni):
            self.utente.appunti.setInformazioni(informazioni)
        else:
            return "Already up-to-date"
        self.salvaAppunti()

    def visualizzaAppunti(self):
        return self.utente.appunto

    def salvaAppunti(self):
        with open(self.utente.appunto.getNome(), "wb") as f:
            pickle.dump(self.utente.appunto, f, pickle.HIGHEST_PROTOCOL)

    def eliminaAppunti(self):
        if os.path.isfile("Appunto.pickle"):
            os.remove("Appunto.pickle")
        else:
            return "File not found"


    def pubblicaAppunti(self):
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
