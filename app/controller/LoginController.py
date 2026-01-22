from PySide6.QtWidgets import QWidget, QMessageBox
from app.views.LoginView_ui import Ui_Form  # <--- OJO: Si te da error, revisa si se llama Ui_Form o Ui_MainWindow en tu ui_login.py
from app.services.AuthService import AuthService

class LoginController(QWidget):
    def __init__(self):
        super().__init__()
        # 1. Cargamos el diseño que hiciste
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 2. Preparamos el servicio de Firebase
        self.auth_service = AuthService()

        # 3. Conectamos el botón
        # Asegúrate de que en QtDesigner llamaste al botón 'btnLogin'
        self.ui.btnLogin.clicked.connect(self.validar_login)

    def validar_login(self):
        # Asegúrate de que tus campos se llaman 'inputEmail' e 'inputPassword'
        email = self.ui.inputEmail.text().strip()
        password = self.ui.inputPassword.text().strip()

        if not email or not password:
            self.ui.lblError.setText("Rellena todos los campos")
            return

        # Llamamos a Firebase
        exito, resultado = self.auth_service.login(email, password)

        if exito:
            # Login correcto
            QMessageBox.information(self, "Login", f"¡Bienvenido!\nID: {resultado}")
            # AQUÍ ES DONDE MÁS ADELANTE ABRIREMOS LA VENTANA 'HOME'
        else:
            # Error (contraseña mal, etc)
            self.ui.lblError.setText(f"Error: {resultado}")