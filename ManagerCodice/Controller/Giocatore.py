import pickle, random
from Model import Utente, Utilities
from Controller import Accesso


class Giocatore:

    def __init__(self, utente:Utente.Utente):
        self.percorso = "Dati-giocatore/"
        self.utente = utente
        self.caricaScheda()
    # TODO Python merda

    def cambioCredenziali(self, nomeUtente, password, id):
        self.accesso = Accesso.Accesso()
        for x in self.accesso.listaUtenti:
            if (nomeUtente == x):
                print("nome utente già esistente")
                return
        self.utente.setNomeUtente(nomeUtente)
        self.utente.setPassword(password)
        self.utente.setId(id)

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

    def aggiornaScheda(self, livello, punteggi, puntiFerita, armatura, tiroSalvezza1, tiroSalvezza2, abilita1, abilita2):
        #TODO forse sarà da cambiare metodo
        competenza = 0
        if self.utente.personaggio.getLivello() != livello:
            competenza = int((livello - 1) / 4 + 2)
            self.utente.personaggio.setLivello(livello)
        if self.utente.personaggio.getPunteggi() != punteggi:
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
            self.utente.personaggio.setTiriSalvezza(salvezza)
        if self.utente.personaggio.getPuntiFerita() != puntiFerita:
            self.utente.personaggio.setPuntiFerita(puntiFerita)
        if self.utente.personaggio.getArmatura() != armatura:
            self.utente.personaggio.setArmatura(armatura)
        self.salvaScheda()

    def visualizzaScheda(self):
            return self.utente.personaggio

    def caricaScheda(self):
        with open("Schede/" + self.utente.getNomeUtente() + ".pickle", "rb") as f:
            self.utente.personaggio = pickle.load(f)

    def salvaScheda(self):
        with open("Schede/" + self.utente.getNomeUtente() + ".pickle", "wb") as f:
            pickle.dump(self.utente.personaggio, f, pickle.HIGHEST_PROTOCOL)

    def tiraDado(self, numeroFacce, numeroLanci):
        self.dado = Utilities.Dado(numeroFacce, numeroLanci)
        return random.randint(1, self.dado.numeroFacce)*self.dado.numeroLanci

    def modificaNote(self, note):
        self.utente.personaggio.setSpazioNote(note)
        self.salvaNote()

    def visualizzaNote(self):
        with open(self.percorso+self.utente.personaggio.getSpazioNote()+".pickle", "rb") as f:
            return pickle.load(f)

    def salvaNote(self):
        with open(self.percorso+self.utente.personaggio.getSpazioNote()+".pickle", "wb") as f:
            pickle.dump(self.utente.personaggio.getSpazioNote(), f, pickle.HIGHEST_PROTOCOL)

    def visualizzaDispense(self):
        #TODO
        pass