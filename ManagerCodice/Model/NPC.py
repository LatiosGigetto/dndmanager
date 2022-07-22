from Model import Appunto


class NPC(Appunto.Appunto):
    def __init__(self):
        super().__init__()
        self.gradoSfida = 0

    def getGradoSfida(self):
        return self.gradoSfida

