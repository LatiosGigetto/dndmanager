import sys

from View import VistaAccesso
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    vistaAccesso = VistaAccesso
    app = QApplication(sys.argv)
    login = QMainWindow()
    ui = VistaAccesso.Ui_Login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

