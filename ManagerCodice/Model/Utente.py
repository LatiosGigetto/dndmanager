import Scheda

class Utente:
    def __init__(self):
        self.id = ""
        self.nomeUtente = ""
        self.password = ""
        self.personaggio = Scheda.Scheda()

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNomeUtente(self):
        return self.nomeUtente

    def setNomeUtente(self, nomeUtente):
        #TODO
        pass

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password
