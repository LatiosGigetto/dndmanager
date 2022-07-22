import os
import pickle
import random

from Model import Utilities, Utente, Appunto, NPC
from Controller import Accesso


class Master:

    def __init__(self, utente):
        self.utente = utente
        self.accesso = Accesso.Accesso()
        self.accesso.caricaListaUtenti()

    def cambioCredenziali(self, nomeUtente, password):
        self.accesso.caricaListaUtenti()
        for x in self.accesso.listaUtenti:
            if nomeUtente == x.nomeUtente:
                return False
        for i in self.accesso.listaUtenti:
            index = self.accesso.listaUtenti.index(i)
            if self.utente.nomeUtente == i.nomeUtente:
                self.utente.setNomeUtente(nomeUtente)
                self.utente.setPassword(password)
                self.accesso.listaUtenti[index] = self.utente
        self.accesso.salvaListaUtenti()
        return True

    def creaAppunti(self, nome, informazioni, isNPC, nomeImmagine=False, gradoSfida=0):
        if isNPC:
            self.appunto = NPC.NPC()
            self.appunto.gradoSfida = gradoSfida
        else:
            self.appunto = Appunto.Appunto()
        self.appunto.setNome(nome)
        if nomeImmagine:
            self.appunto.setImmagine(nomeImmagine)
        self.appunto.setInformazioni(informazioni)
        self.salvaAppunti()

    def visualizzaAppunti(self, nomeAppunto):
        if self.caricaAppunti(nomeAppunto):
            return self.appunto
        else:
            return "File not found"

    def eliminaAppunti(self, nomeAppunto):
        if os.path.isfile("Appunti/" + nomeAppunto + ".pickle"):
            os.remove("Appunti/" + nomeAppunto + ".pickle")
            if os.path.isfile("Appunti/" + nomeAppunto + ".jpg"):
                os.remove("Appunti/" + nomeAppunto + ".jpg")
        self.appunto = Appunto.Appunto()

    def salvaAppunti(self):
        with open("Appunti/" + self.appunto.getNome() + ".pickle", "wb") as f:
            pickle.dump(self.appunto, f, pickle.HIGHEST_PROTOCOL)


    def caricaAppunti(self, nomeAppunto):
        if os.path.isfile("Appunti/" + nomeAppunto + ".pickle"):
            with open("Appunti/" + nomeAppunto + ".pickle", "rb") as f:
                self.appunto = pickle.load(f)
            return True
        return False

    def pubblicaAppunti(self, nomeAppunto):
        if self.caricaAppunti(nomeAppunto):
            self.appunto.setIspublic(True)
            self.salvaAppunti()
            return True
        return "File not found"

    def trovaPersonaggi(self, nomeUtente):
        for i in self.accesso.listaUtenti:
            if nomeUtente == i.nomeUtente:
                if i.isMaster:
                    return False
                return i
        return False

    def visualizzaPersonaggi(self, nomePersonaggio):
        if self.trovaPersonaggi(nomePersonaggio):
            return self.utente.personaggio
        return "File not found"

    def tiraDado(self, numeroFacce, numeroLanci):
        self.dado = Utilities.Dado(int(numeroFacce), int(numeroLanci))
        return str(random.randint(1, self.dado.numeroFacce) * self.dado.numeroLanci)

    def caricaContatore(self):
        contatore = 0
        if os.path.isfile("contatore.txt"):
            with open("contatore.txt") as fileContatore:
                contatore = int(fileContatore.read())
                fileContatore.close()
        self.contatoreAttuale = Utilities.Contatore(contatore)

    def incrementaContatore(self):
        self.contatoreAttuale.contatore += 1

    def resettaContatore(self):
        self.contatoreAttuale.contatore = 0

    def visualizzaContatore(self):
        if self.contatoreAttuale.contatore < 0:
            self.resettaContatore()
        return str(self.contatoreAttuale.contatore)

    def salvaContatore(self):
        fileContatore = open("contatore.txt", 'w')
        fileContatore.write(str(self.contatoreAttuale.contatore))
        fileContatore.close()

    def creaStatistiche(self):
        self.accesso.caricaListaUtenti()
        numGiocatori = 0
        mediaPF = 0
        mediaCA = 0
        mediaLivello = 0
        mediaFor = 0
        mediaDes = 0
        mediaCos = 0
        mediaInt = 0
        mediaSag = 0
        mediaCar = 0

        for i in self.accesso.listaUtenti:
            if i.isMaster or i.personaggio.getNome() == "":
                continue
            numGiocatori += 1
            mediaPF += i.personaggio.getPuntiFerita()
            mediaCA += i.personaggio.getArmatura()
            mediaLivello += i.personaggio.getLivello()
            mediaFor += i.personaggio.punteggi["Forza"]
            mediaDes += i.personaggio.punteggi["Destrezza"]
            mediaCos += i.personaggio.punteggi["Costituzione"]
            mediaInt += i.personaggio.punteggi["Intelligenza"]
            mediaSag += i.personaggio.punteggi["Saggezza"]
            mediaCar += i.personaggio.punteggi["Carisma"]
        if numGiocatori == 0:
            return False
        finalPF = int(mediaPF / numGiocatori)
        finalCA = int(mediaCA / numGiocatori)
        finalLivello = int(mediaLivello / numGiocatori)
        finalFor = int(mediaFor / numGiocatori)
        finalDes = int(mediaDes / numGiocatori)
        finalCos = int(mediaCos / numGiocatori)
        finalInt = int(mediaInt / numGiocatori)
        finalSag = int(mediaSag / numGiocatori)
        finalCar = int(mediaCar / numGiocatori)
        return finalPF, finalCA, finalLivello, finalFor, finalDes, finalCos, finalInt, finalSag, finalCar



