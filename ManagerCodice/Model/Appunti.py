from PIL import Image


class Appunti:
    def __init__(self):
        self.immagine = Image
        self.informazioni = ""
        self.nome = ""

    def getImmagine(self):
        return self.immagine

    def setImmagine(self, immagine):
        #TODO
        pass

    def getInformazioni(self):
        return self.informazioni

    def setInformazioni(self, informazioni):
        #TODO
        pass

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome