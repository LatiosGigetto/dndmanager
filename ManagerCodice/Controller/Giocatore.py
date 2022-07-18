import pickle, random
from Model import Utente, Utilities


class Giocatore:

    utente = Utente.Utente()    #creazione dell'oggetto ridondante perché è il costruttore che lo farà poi (parte da rivedere)

    def __init__(self, utente):
       self.utente = utente
    # TODO Python merda

    def cambioCredenziali(self, nomeUtente, password, id):
        self.utente.setNomeUtente(self, nomeUtente)
        self.utente.setPassword(self, password)
        self.utente.setId(self, id)

    def creaScheda(self, nome, punteggi, classe, livello, puntiFerita, armatura, tiroSalvezza1, tiroSalvezza2, abilita1, abilita2, storia):
        competenza = int((livello-1)/4 + 2)
        self.utente.personaggio.setNome(nome)
        self.utente.personaggio.setClasse(classe)
        self.utente.personaggio.setLivello(livello)
        self.utente.personaggio.setPuntiFerita(puntiFerita)
        self.utente.personaggio.setArmatura(armatura)
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

    def aggiornaScheda(self):
        #TODO
        self.salvaScheda()
        pass

    def visualizzaScheda(self):
        #TODO
        return self.utente.personaggio

    def salvaScheda(self):
        with open(self.utente.personaggio.getNome(), "wb") as f:
            pickle.dump(self.utente.personaggio, f, pickle.HIGHEST_PROTOCOL)

    def tiraDado(self, numeroFacce, numeroLanci):
        self.dado = Utilities.Dado(numeroFacce, numeroLanci)
        return random.randint(1, self.dado.numeroFacce)*self.dado.numeroLanci

    def modificaNote(self):
        #TODO
        self.salvaNote()

    def visualizzaNote(self):
        #TODO
        pass

    def salvaNote(self):
        #TODO
        pass

    def visualizzaDispense(self):
        #TODO
        pass