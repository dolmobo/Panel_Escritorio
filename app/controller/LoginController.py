from PySide6.QtWidgets import QWidget, QMessageBox
from app.views.LoginView_ui import Ui_LoginView
from app.services.AuthService import AuthService
from app.controller.MainController import MainController
from app.services.SettingsService import SettingsService  # <--- Nuevo import
from translations import TRADUCCIONES                       # <--- Nuevo import

class LoginController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginView()
        self.ui.setupUi(self)
        
        self.auth_service = AuthService()
        
        # 1. Cargar Configuración de Idioma
        self.settings_service = SettingsService()
        self.current_lang = self.settings_service.state.get("language", "Español")
        
        # 2. Aplicar Traducción Inicial
        self.retraducir_ui()
        
        # 3. Limpiar estilos del Designer (para que el tema global funcione bien)
        if hasattr(self.ui, 'input_user'): self.ui.input_user.setStyleSheet("")
        if hasattr(self.ui, 'input_password'): self.ui.input_password.setStyleSheet("")
        if hasattr(self.ui, 'btn_login'): self.ui.btn_login.setStyleSheet("")

        # Conexiones
        self.ui.btn_login.clicked.connect(self.manejar_login)

    def retraducir_ui(self):
        """Traduce la pantalla de Login según el idioma guardado"""
        t = TRADUCCIONES.get(self.current_lang, TRADUCCIONES["Español"])

        self.ui.label_title.setText(t["login_title"])

        self.ui.input_user.setPlaceholderText(t["login_user_ph"])

        self.ui.input_password.setPlaceholderText(t["login_pass_ph"])

        self.ui.btn_login.setText(t["login_btn"])

    def manejar_login(self):
        user = self.ui.input_user.text()
        password = self.ui.input_password.text()

        # Usamos el diccionario para los mensajes de error también
        t = TRADUCCIONES.get(self.current_lang, TRADUCCIONES["Español"])

        uid, result = self.auth_service.login(user, password)

        if uid:
            self.main_win = MainController(user_name=result, user_id=uid)
            self.main_win.show()
            self.close()
        else:
            # Mensaje de error traducido
            QMessageBox.warning(self, t["login_error_title"], t["login_error_msg"])