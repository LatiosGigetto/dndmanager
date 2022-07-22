import unittest

from Controller import Accesso
from Model import Utente

class MyTestCase(unittest.TestCase):
    def testCaricaLista(self):
        accesso = Accesso.Accesso()

        self.assertTrue(accesso.caricaListaUtenti())

    def testLogin(self):
        accesso = Accesso.Accesso()

        self.assertIsInstance(accesso.login("nomeTest", "passwordTest"), type(Utente.Utente()))

        self.assertEqual(accesso.login("nomeTest", "passErrata"), "Password")

        self.assertEqual(accesso.login("nomeErrato", "passwordTest"), "Utente")



if __name__ == '__main__':
    unittest.main()
