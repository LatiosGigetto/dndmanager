class Scheda:

    def __init__(self):
        self.nome = ""
        self.armatura = 0
        self.classe = ""
        self.livello = 1
        self.punteggi = {
            "Forza" : 0,
            "Destrezza" : 0,
            "Costituzione" : 0,
            "Intelligenza" : 0,
            "Saggezza" : 0,
            "Carisma" : 0
        }
        self.abilita = {
            "Acrobazia" : 0,
            "Addestrare Animali" : 0,
            "Arcano" : 0
,           "Atletica" : 0,
            "Furtività" : 0,
            "Indagare" : 0,
            "Inganno" : 0,
            "Intimidire" : 0,
            "Intrattenere" : 0,
            "Intuizione" : 0,
            "Medicina" : 0,
            "Natura" : 0,
            "Percezione" : 0,
            "Persuasione" : 0,
            "Rapidità di Mano" : 0,
            "Religione" : 0,
            "Sopravvivenza" : 0,
            "Storia" : 0
        }
        self.puntiFerita = 0
        self.salvezza = {
            "Forza" : 0,
            "Destrezza" : 0,
            "Costituzione" : 0,
            "Intelligenza" : 0,
            "Saggezza" : 0,
            "Carisma" : 0
        }
        self.spazioNote = ""
        self.storia = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getAbilita (self):
        return self.abilita

    def setAbilita (self, abilita):
        self.abilita = abilita

    def getArmatura(self):
        return self.armatura

    def setArmatura(self, armatura):
        self.armatura = armatura

    def getClasse(self):
        return self.classe

    def setClasse(self, classe):
        self.classe = classe

    def getLivello(self):
        return self.livello

    def setLivello(self, livello):
        self.livello = livello

    def getPunteggi(self):
        return self.punteggi

    def setPunteggi(self, punteggi):
        self.punteggi = punteggi

    def getPuntiFerita(self):
        return self.puntiFerita

    def setPuntiFerita(self, puntiFerita):
        self.puntiFerita = puntiFerita

    def getTiriSalvezza(self):
        return self.salvezza

    def setTiriSalvezza(self, salvezza):
        self.salvezza = salvezza

    def getSpazioNote(self):
        return self.spazioNote

    def setSpazioNote(self, spazioNote):
        self.spazioNote = spazioNote

    def getStoria(self):
        return self.storia

    def setStoria(self, storia):
        self.storia = storia