import os
from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox
from PySide6.QtGui import QPixmap

# Vistas UI
from app.views.MainView_ui import Ui_MainView
from app.views.DashBoardView_ui import Ui_DashboardView 
from app.views.ReportView_ui import Ui_ReportsView
from app.views.SettingView_ui import Ui_SettingsView

from app.services.DataService import DataService

from app.controller.PanelController import PanelController 
from app.controller.ReportController import ReportController
from app.controller.SettingsController import SettingsController

class MainController(QMainWindow):
    def __init__(self, user_name="Usuario", user_id=None):
        super().__init__()
        self.ui = Ui_MainView()
        self.ui.setupUi(self)
        
        self.data_service = DataService()
        self.user_name = user_name
        self.user_id = user_id 

        self.init_sub_views()
        self.cargar_logo()

        self.ctrl_dashboard = PanelController(self) 

        self.ctrl_reports = ReportController(self)
        self.ctrl_settings = SettingsController(self)

        self.ui.btn_dashboard.clicked.connect(lambda: self.cambiar_pagina(0))
        self.ui.btn_reports.clicked.connect(self.ir_a_reportes)
        self.ui.btn_settings.clicked.connect(lambda: self.cambiar_pagina(2))
        self.ui.btn_exit.clicked.connect(self.manejar_logout)

        self.ui.stack_content.setCurrentIndex(0)

    def init_sub_views(self):
        # Página 1: Dashboard
        self.page_dashboard = QWidget()
        self.ui_dashboard = Ui_DashboardView()
        self.ui_dashboard.setupUi(self.page_dashboard)
        self.ui.stack_content.addWidget(self.page_dashboard)
        
        # Página 2: Reportes
        self.page_reports = QWidget()
        self.ui_reports = Ui_ReportsView()
        self.ui_reports.setupUi(self.page_reports)
        self.ui.stack_content.addWidget(self.page_reports)

        # Página 3: Ajustes
        self.page_settings = QWidget()
        self.ui_settings = Ui_SettingsView()
        self.ui_settings.setupUi(self.page_settings)
        self.ui.stack_content.addWidget(self.page_settings)

    def cambiar_pagina(self, index):
        self.ui.stack_content.setCurrentIndex(index)

    def ir_a_reportes(self):
        """Cambia de página y pide al controlador de reportes que actualice los datos"""
        self.cambiar_pagina(1)
        # Nos aseguramos de que el método exista antes de llamarlo para evitar crasheos
        if hasattr(self.ctrl_reports, 'actualizar_datos'):
            self.ctrl_reports.actualizar_datos()

    def manejar_logout(self):
        from app.controller.LoginController import LoginController
        if QMessageBox.question(self, "Salir", "¿Cerrar sesión?") == QMessageBox.StandardButton.Yes:
            self.login_win = LoginController()
            self.login_win.show()
            self.close()

    def cargar_logo(self):
        r = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logo.png")
        if os.path.exists(r):
            self.ui.label_logo.setPixmap(QPixmap(r))
            self.ui.label_logo.setScaledContents(True)