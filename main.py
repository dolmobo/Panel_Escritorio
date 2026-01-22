import sys
from PySide6.QtWidgets import QApplication
from app.controller.LoginController import LoginController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Creamos y mostramos el controlador del Login
    ventana = LoginController()
    ventana.show()
    
    sys.exit(app.exec())