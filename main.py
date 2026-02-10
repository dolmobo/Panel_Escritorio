import sys
from PySide6.QtWidgets import QApplication
from app.controller.LoginController import LoginController
from app.services.SettingsService import SettingsService
from app.styles.StyleManager import StyleManager

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    settings_service = SettingsService()
    
    tema_guardado = settings_service.state.get("theme", "Claro")
    
    StyleManager.aplicar_tema(tema_guardado)
    
    ventana = LoginController()
    ventana.show()
    
    sys.exit(app.exec())