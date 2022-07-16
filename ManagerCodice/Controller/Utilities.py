import random

class Dado:

    def __init__(self, numeroFacce, numeroLanci):
        self.numeroFacce = numeroFacce
        self.numeroLanci = numeroLanci

    def lancioDadi(self):
        return random.randint(1, self.numeroFacce)*self.numeroLanci


class Contatore:

    def __init__(self, contatoreCorrente):
        self.contatore = contatoreCorrente

    def incrementaContatore(self):
        self.contatore += 1

    def resettaContatore(self):
        self.contatore = 0

    def visualizzaContatore(self):
        return self.contatore
