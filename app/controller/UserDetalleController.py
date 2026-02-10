from PySide6.QtWidgets import QDialog, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

from app.views.UserDetailsView_ui import Ui_UserDetailsDialog

class UserDetailsController(QDialog):
    def __init__(self, datos_usuario, parent=None):
        super().__init__(parent)
        self.ui = Ui_UserDetailsDialog()
        self.ui.setupUi(self)

        # Configuración de ventana (Sin bordes nativos, fondo transparente)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Sombra bonita
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(5)
        shadow.setColor(QColor(0, 0, 0, 80))
        
        # Aplicamos la sombra al Frame interior (frame_card)
        self.ui.frame_card.setGraphicsEffect(shadow)

        # Rellenar datos
        self.cargar_datos(datos_usuario)

        # Conectar botón
        self.ui.btn_close.clicked.connect(self.close)

    def cargar_datos(self, datos):
        """Rellena los labels con la información del diccionario"""
        nombre = datos.get('username', 'Desconocido').upper()
        self.ui.lbl_username.setText(nombre)
        
        self.ui.lbl_record.setText(f"{datos.get('record', 0)} pts")
        self.ui.lbl_games.setText(str(datos.get('partidas_totales', 0)))
        self.ui.lbl_jumps.setText(str(datos.get('saltos_totales', 0)))
        self.ui.lbl_coins.setText(str(datos.get('monedas', 0)))