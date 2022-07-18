import random, os
from Model import Utilities,Utente

class Master:

    utente = Utente.Utente()  # creazione dell'oggetto ridondante perché è il costruttore che lo farà poi (parte da rivedere)

    def __init__(self, utente):
        self.utente = utente
    # TODO Python merda

    def cambioCredenziali(self, nomeUtente, password, id):
        self.utente.setNomeUtente(self, nomeUtente)
        self.utente.setPassword(self, password)
        self.utente.setId(self, id)

    def creaAppunti(self):
        #TODO
        pass

    def aggiornaAppunti(self):
        #TODO
        pass

    def visualizzaAppunti(self):
        #TODO
        pass

    def salvaAppunti(self):
        #TODO
        pass

    def eliminaAppunti(self):
        #TODO
        pass

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
