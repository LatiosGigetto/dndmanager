from PIL import Image


class Appunti:
    def __init__(self):
        self.immagine = Image
        self.informazioni = ""
        self.nome = ""
        self.ispublic = False
    def getImmagine(self):
        return self.immagine

    def setImmagine(self, immagine):
        #TODO
        pass

    def getInformazioni(self):
        return self.informazioni

    def setInformazioni(self, informazioni):
        self.informazioni = informazioni

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getIspublic(self):
        return  self.ispublic

    def setIspublic(self, ispublic):
        self.ispublic = ispublic