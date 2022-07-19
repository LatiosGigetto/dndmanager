import os.path
import pickle
from random import randint

from Model.Utente import Utente


class Accesso:

    def __init__(self):
        self.listaUtenti = []

    def caricaListaUtenti(self):
        if os.path.isfile("listaUtenti.pickle"):
            with open("listaUtenti.pickle", "rb") as f:
                self.listaUtenti.pickle.load(f)
        return

    def salvaListaUtenti(self):
        with open("listaUtenti.pickle", "wb") as f:
            pickle.dump(self.listaUtenti, f, pickle.HIGHEST_PROTOCOL)

    def registrazione(self, nomeUtente, password):
        self.caricaListaUtenti()
        for i in self.listaUtenti:
            if nomeUtente == i.nomeUtente:
                return False
            else:
                continue
        id = str(randint(1000, 9999))
        i = 0
        while i < len(self.listaUtenti):
            if self.listaUtenti(i).id == id:
               id = str(randint(1000, 9999))
               i = 0
            else:
                i += 1
                continue
            utente = Utente(nomeUtente, password, id)
            self.listaUtenti.append(utente)
            self.salvaListaUtenti()
            return True

    def login(self, nomeUtente, password):
        self.caricaListaUtenti()
        for i in self.listaUtenti:
            if nomeUtente == i.nomeUtente:
                if password == i.password:
                    if i.isMaster:
                        print()
                        # TODO Inserisci apertura vista Master
                    else:
                        print()
                        # TODO Inserisci apertura vista Giocatore
                else:
                    print("Password errata.")
                    return False
            else:
                continue
            print("Nome utente non trovato")
            return False





