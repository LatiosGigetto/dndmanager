import pickle

from Model import Utente, Scheda


class Giocatore:

    def __init__(self, utente):
        self.idUtenteCorrente = utente.Utente.getId
        self.utenteAttivo = utente

    # TODO Python merda

    def salvaScheda(self, personaggio):
        with open(personaggio.getNome(), "wb") as f:
            pickle.dump(personaggio, f, pickle.HIGHEST_PROTOCOL)

    def creaScheda(self, nome, punteggi, classe, livello, puntiFerita, armatura, tiroSalvezza1, tiroSalvezza2, abilita1, abilita2, storia):
        personaggio = Scheda()
        competenza = int((livello-1)/4 + 2)
        personaggio.setNome(nome)
        personaggio.setClasse(classe)
        personaggio.setLivello(livello)
        personaggio.setPuntiFerita(puntiFerita)
        personaggio.setArmatura(armatura)
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
        personaggio.setTiriSalvezza(salvezza)
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
        personaggio.setAbilita(abilita)
        personaggio.setStoria(storia)
        self.salvaScheda(personaggio)
