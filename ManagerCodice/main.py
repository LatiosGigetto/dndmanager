import sys

from View import VistaAccesso
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    import sys
    vistaAccesso = VistaAccesso
    app = QApplication(sys.argv)
    Login = QMainWindow()
    ui = VistaAccesso.Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

