import os.path
import pickle, random
from Model import Utente, Utilities
from Controller import Accesso


class Giocatore:

    def __init__(self, utente):
        self.accesso = Accesso.Accesso()
        self.utente = utente
        self.caricaScheda()
    # TODO Python merda

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

    def creaScheda(self, nome, punteggi, classe, livello, puntiFerita, armatura, tiroSalvezza1, tiroSalvezza2, abilita1, abilita2, storia):
        competenza = int((livello-1)/4 + 2)
        self.utente.personaggio.setNome(nome)
        self.utente.personaggio.setClasse(classe)
        self.utente.personaggio.setLivello(livello)
        self.utente.personaggio.setPuntiFerita(puntiFerita)
        self.utente.personaggio.setArmatura(armatura)
        self.utente.personaggio.setPunteggi(punteggi)
        salvezza = {
            "Forza" : int(punteggi["Forza"]-10 / 2),
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
            "Acrobazia" : int(punteggi["Destrezza"] - 10 / 2),
            "Addestrare Animali" : int(punteggi["Saggezza"] - 10 / 2),
            "Arcano" : int(punteggi["Intelligenza"] - 10 / 2),
            "Atletica" : int(punteggi["Forza"]-10 / 2),
            "Furtività" : int(punteggi["Destrezza"] - 10 / 2),
            "Indagare" : int(punteggi["Intelligenza"] - 10 / 2),
            "Inganno" : int(punteggi["Carisma"] - 10 / 2),
            "Intimidire" : int(punteggi["Carisma"] - 10 / 2),
            "Intrattenere" : int(punteggi["Carisma"] - 10 / 2),
            "Intuizione" : int(punteggi["Saggezza"] - 10 / 2),
            "Medicina" : int(punteggi["Saggezza"] - 10 / 2),
            "Natura" : int(punteggi["Intelligenza"] - 10 / 2),
            "Percezione" : int(punteggi["Saggezza"] - 10 / 2),
            "Persuasione" : int(punteggi["Carisma"] - 10 / 2),
            "Rapidità di Mano" : int(punteggi["Destrezza"] - 10 / 2),
            "Religione" : int(punteggi["Intelligenza"] - 10 / 2),
            "Sopravvivenza" : int(punteggi["Saggezza"] - 10 / 2),
            "Storia" : int(punteggi["Intelligenza"] - 10 / 2)
        }
        abilita[abilita1] += competenza
        abilita[abilita2] += competenza
        self.utente.personaggio.setAbilita(abilita)
        self.utente.personaggio.setStoria(storia)
        self.salvaScheda()
        for i in self.accesso.listaUtenti:
            index = self.accesso.listaUtenti.index(i)
            if self.utente.nomeUtente == i.nomeUtente:
                self.accesso.listaUtenti[index] = self.utente
        self.accesso.salvaListaUtenti()

    def caricaScheda(self):
        if os.path.isfile("Schede/" + self.utente.personaggio.getNome() + ".pickle"):
            with open("Schede/" + self.utente.personaggio.getNome() + ".pickle", "rb") as f:
                self.utente.personaggio = pickle.load(f)
                return True
        else:
            return False

    def visualizzaScheda(self):
        self.caricaScheda()
        return self.utente.personaggio

    def salvaScheda(self):
        with open("Schede/" + self.utente.personaggio.getNome() + ".pickle", "wb") as f:
            pickle.dump(self.utente.personaggio, f, pickle.HIGHEST_PROTOCOL)
        self.accesso.caricaListaUtenti()
        self.accesso.salvaListaUtenti()

    def tiraDado(self, numeroFacce, numeroLanci):
        self.dado = Utilities.Dado(int(numeroFacce), int(numeroLanci))
        return str(random.randint(1, self.dado.numeroFacce)*self.dado.numeroLanci)

    def modificaNote(self, note):
        self.utente.personaggio.setSpazioNote(note)
        self.salvaNote()

    def visualizzaNote(self):
        self.caricaScheda()
        return self.utente.personaggio.getSpazioNote()

    def salvaNote(self):
        with open("Schede/" + self.utente.personaggio.getNome() + ".pickle", "wb") as f:
            pickle.dump(self.utente.personaggio, f, pickle.HIGHEST_PROTOCOL)
