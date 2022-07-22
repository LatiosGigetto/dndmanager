import unittest

from Model import Utente, Utilities
from Controller import Master


class TestControllerMaster(unittest.TestCase):
    def testCambioCredenziali(self):
        master = Utente.Utente()
        controller = Master.Master(master)

        master.setNomeUtente("Test")
        master.setPassword("Test")
        lista = [master]

        controller.accesso.listaUtenti = lista
        controller.accesso.salvaListaUtenti()


        controller.cambioCredenziali("nomeTest", "passwordTest")

        self.assertIs(master.nomeUtente, "nomeTest")
        self.assertIs(master.password, "passwordTest")

    def testContatore(self):
        master = Utente.Utente()
        controller = Master.Master(master)

        controller.caricaContatore()
        controller.incrementaContatore()
        controller.resettaContatore()
        controller.incrementaContatore()
        controller.incrementaContatore()

        self.assertEqual(controller.contatoreAttuale.contatore, 2)

    def testDadi(self):
        master = Utente.Utente()
        controller = Master.Master(master)

        risultato = controller.tiraDado(4, 2)

        self.assertIsNot(risultato, "9")



if __name__ == '__main__':
    unittest.main()
