import random, os
from Model import Utilities

class Master:

    def caricaContatore(self):
        contatore = 0
        if (os.path.exists("readme.txt")):
            with open("readme.txt") as f:
                contatore = f.read()
        f.close()
        self.contatoreAttuale = Utilities.Contatore(contatore)

    def aggiornaScheda(self):
        #TODO
        pass

    def aggiornaPersonaggi(self):
        #TODO
        pass

    def creaAppunti(self):
        #TODO
        pass

    def cambioCredenziali(self):
        #TODO
        pass

    def creaStatistiche(self):
        #TODO
        pass

    def eliminaAppunti(self):
        #TODO
        pass

    def incrementaContatore(self):
        self.contatoreAttuale.contatore += 1

    def resettaContatore(self):
        self.contatoreAttuale.contatore = 0

    def visualizzaContatore(self):
        if (self.contatoreAttuale.contatore < 0):
            self.resettaContatore()
        return self.contatoreAttuale.contatore

    def pubblicaAppunti(self):
        #TODO
        pass

    def tiraDado(self, numeroFacce, numeroLanci):
        self.dado = Utilities.Dado(numeroFacce, numeroLanci)
        return random.randint(1, self.dado.numeroFacce) * self.dado.numeroLanci

    def visualizzaAppunti(self):
        #TODO
        pass

    def visualizzaPersonaggi(self):
        #TODO
        pass


