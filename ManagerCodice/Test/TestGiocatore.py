import os.path
import unittest
from Controller import Giocatore
from Model import Utente, Scheda


class TestControllerGiocatore(unittest.TestCase):
    def testCreaScheda(self):
        utente = Utente.Utente()
        controller = Giocatore.Giocatore(utente)

        controller.creaScheda("Test", utente.personaggio.punteggi, "Barbaro", 1, 12, 12, "Forza", "Destrezza",
                              "Acrobazia", "Percezione", "Storia Test")

        self.assertTrue(os.path.isfile("Schede/Test.pickle"))

    def testVisualizzaScheda(self):
        utente = Utente.Utente()
        controller = Giocatore.Giocatore(utente)

        self.assertIsInstance(controller.visualizzaScheda(), Scheda.Scheda)

    def testCaricaScheda(self):
        utente1 = Utente.Utente()
        utente2 = Utente.Utente()
        controller1 = Giocatore.Giocatore(utente1)
        controller2 = Giocatore.Giocatore(utente2)

        utente1.personaggio.setNome("Grullo")

        self.assertTrue(controller1.caricaScheda())
        self.assertFalse(controller2.caricaScheda())


if __name__ == '__main__':
    unittest.main()
