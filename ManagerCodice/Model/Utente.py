from Model import Scheda, Appunti

class Utente:
    def __init__(self):
        self.id = ""
        self.nomeUtente = ""
        self.password = ""
        self.personaggio = Scheda.Scheda()
        self.appunto = Appunti.Appunti()
        self.isMaster = False

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNomeUtente(self):
        return self.nomeUtente

    def setNomeUtente(self, nomeUtente):
        self.nomeUtente = nomeUtente

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password
