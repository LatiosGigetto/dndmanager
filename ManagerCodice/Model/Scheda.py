class Scheda:
    def __init__(self):
        self.abilita = ();
        self.armatura = 0;
        self.classe = "";
        self.livello = 1;
        self.punteggi = ();
        self.puntiFerita = 0;
        self.salvezza = ();
        self.spazioNote = "";
        self.storia = {};

    @property
    def getAbilita (self):
        return self.abilita

    @.setter
    def setAbilita (self, abilita):
        pass

    @property
    def getArmatura(self):
        return self.armatura

    @.setter
    def setArmatura(self, armatura):
        pass

    @property
    def getClasse(self):
        return self.classe

    @.setter
    def setClasse(self, classe):
        pass

    @property
    def getLivello(self):
        return self.livello

    @.setter
    def setLivello(self, livello):
        pass

    @property
    def getPunteggi(self):
        return self.classe

    @.setter
    def setPunteggi(self, punteggi):
        pass

    @property
    def getPuntiFerita(self):
        return self.classe

    @.setter
    def setPuntiFerita(self, puntiFerita):
        pass

    @property
    def getSalvezza(self):
        return self.salvezza

    @.setter
    def setSalvezza(self, salvezza):
        pass

    @property
    def getSpazioNote(self):
        return self.spazioNote

    @.setter
    def setSpazioNote(self, spazioNote):
        pass

    @property
    def getStoria(self):
        return self.storia

    @.setter
    def setStoria(self, storia):
        pass