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

    def aggiornaAppunti(self, nomeAppunto, immagine, informazioni):
        if self.caricaAppunti(nomeAppunto):
            if self.appunto.getImmagine() != immagine:
                self.appunto.setImmagine(immagine)
            else:
                return "Already up-to-date"
            if self.appunto.getInformazioni() != informazioni:
                self.appunto.setInformazioni(informazioni)
            else:
                return "Already up-to-date"
            self.salvaAppunti()
            return "File updated"
        return "File not found"

    def eliminaAppunti(self, nomeAppunto):
        if self.caricaAppunti(nomeAppunto):
            os.remove("Appunti/" + nomeAppunto + ".pickle")
            return "File removed"
        else:
            return "File not found"

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
            if i.isMaster:
                return False
            if nomeUtente == i.nomeUtente:
                return i
        return False

    def aggiornaPersonaggio(self, nome, punteggi, classe, livello, puntiFerita, armatura, tiroSalvezza1, tiroSalvezza2, abilita1,
                   abilita2, storia):
        competenza = int((livello - 1) / 4 + 2)
        self.utente.personaggio.setNome(nome)
        self.utente.personaggio.setClasse(classe)
        self.utente.personaggio.setLivello(livello)
        self.utente.personaggio.setPuntiFerita(puntiFerita)
        self.utente.personaggio.setArmatura(armatura)
        self.utente.personaggio.setPunteggi(punteggi)
        salvezza = {
            "Forza": int(punteggi["Forza"] - 10 / 2),
            "Destrezza": int(punteggi["Destrezza"] - 10 / 2),
            "Costituzione": int(punteggi["Costituzione"] - 10 / 2),
            "Intelligenza": int(punteggi["Intelligenza"] - 10 / 2),
            "Saggezza": int(punteggi["Saggezza"] - 10 / 2),
            "Carisma": int(punteggi["Carisma"] - 10 / 2)
        }
        salvezza[tiroSalvezza1] += competenza
        salvezza[tiroSalvezza2] += competenza
        self.utente.personaggio.setTiriSalvezza(salvezza)
        abilita = {
            "Acrobazia": int(punteggi["Destrezza"] - 10 / 2),
            "Addestrare Animali": int(punteggi["Saggezza"] - 10 / 2),
            "Arcano": int(punteggi["Intelligenza"] - 10 / 2),
            "Atletica": int(punteggi["Forza"] - 10 / 2),
            "Furtività": int(punteggi["Destrezza"] - 10 / 2),
            "Indagare": int(punteggi["Intelligenza"] - 10 / 2),
            "Inganno": int(punteggi["Carisma"] - 10 / 2),
            "Intimidire": int(punteggi["Carisma"] - 10 / 2),
            "Intrattenere": int(punteggi["Carisma"] - 10 / 2),
            "Intuizione": int(punteggi["Saggezza"] - 10 / 2),
            "Medicina": int(punteggi["Saggezza"] - 10 / 2),
            "Natura": int(punteggi["Intelligenza"] - 10 / 2),
            "Percezione": int(punteggi["Saggezza"] - 10 / 2),
            "Persuasione": int(punteggi["Carisma"] - 10 / 2),
            "Rapidità di Mano": int(punteggi["Destrezza"] - 10 / 2),
            "Religione": int(punteggi["Intelligenza"] - 10 / 2),
            "Sopravvivenza": int(punteggi["Saggezza"] - 10 / 2),
            "Storia": int(punteggi["Intelligenza"] - 10 / 2)
        }
        abilita[abilita1] += competenza
        abilita[abilita2] += competenza
        self.utente.personaggio.setAbilita(abilita)
        self.utente.personaggio.setStoria(storia)
        self.salvaPersonaggio()

    def salvaPersonaggio(self):
        with open("Schede/" + self.utente.getNomeUtente() + ".pickle", "wb") as f:
            pickle.dump(self.utente.personaggio, f, pickle.HIGHEST_PROTOCOL)

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



