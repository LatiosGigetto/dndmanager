import os.path
import pickle
from random import randint

from Model import Utente


class Accesso:

    def __init__(self):
        self.listaUtenti = []

    def caricaListaUtenti(self):
        if os.path.isfile("listaUtenti.pickle"):
            with open("listaUtenti.pickle", "rb") as f:
                self.listaUtenti = pickle.load(f)
                return True
        return False

    def salvaListaUtenti(self):
        with open("listaUtenti.pickle", "wb") as f:
            pickle.dump(self.listaUtenti, f, pickle.HIGHEST_PROTOCOL)

    def registrazione(self, nomeUtente, password):
        isPlayer = self.caricaListaUtenti()
        if self.listaUtenti:
            for i in self.listaUtenti:
                if nomeUtente == i.nomeUtente:
                    return False
        id = str(randint(1000, 9999))
        i = 0
        while i < len(self.listaUtenti):
            if self.listaUtenti[i].id == id:
                id = str(randint(1000, 9999))
                i = 0
            else:
                i += 1
                continue
        utente = Utente.Utente()
        utente.setNomeUtente(nomeUtente)
        utente.setPassword(password)
        utente.setId(id)
        if not isPlayer:
            utente.isMaster = True
        self.listaUtenti.append(utente)
        self.salvaListaUtenti()
        return utente

    def login(self, nomeUtente, password):
        self.caricaListaUtenti()
        for i in self.listaUtenti:
            if nomeUtente == i.nomeUtente:
                if password == i.password:
                        return i
                else:
                    return "Password"
        return "Utente"





