import Scheda
class Utente:
    def __init__(self):
        self.id = "";
        self.nomeUtente = "";
        self.password = "";
        self.personaggio = Scheda();

    @property
    def getId (self):
        return self.id

    @.setter
    def setId (self, id):
        pass

    @property
    def getNomeUtente(self):
        return self.nomeUtente

    @.setter
    def setNomeUtente(self, nomeUtente):
        pass

    @property
    def getPassword(self):
        return self.Password

    @.setter
    def setPassword(self, password):
        pass
