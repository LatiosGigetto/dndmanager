import os.path

from PIL import Image


class Appunto:
    def __init__(self):
        self.immagine = None
        self.informazioni = ""
        self.nome = ""
        self.ispublic = False
    def getImmagine(self):
        return self.immagine

    def setImmagine(self, nomeImmagine):
        self.immagine = Image.open(nomeImmagine)
        self.immagine.load()
        self.immagine.save("./Appunti/" + self.nome + ".jpg", "JPEG")

    def getInformazioni(self):
        return self.informazioni

    def setInformazioni(self, informazioni):
        self.informazioni = informazioni

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getIspublic(self):
        return self.ispublic

    def setIspublic(self, ispublic):
        self.ispublic = ispublic