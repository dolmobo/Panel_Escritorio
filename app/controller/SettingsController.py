from PySide6.QtWidgets import QWidget, QApplication
from app.services.SettingsService import SettingsService
from app.styles.StyleManager import StyleManager
from translations import TRADUCCIONES

class SettingsController:
    def __init__(self, main_controller):
        self.main = main_controller
        self.ui = self.main.ui_settings
        self.service = SettingsService()

        # Carga inicial
        self.aplicar_ajustes_completos()
        
        # Conexiones
        self.ui.combo_theme.currentIndexChanged.connect(self.guardar_y_actualizar)
        self.ui.combo_language.currentIndexChanged.connect(self.guardar_y_actualizar)

    def aplicar_ajustes_completos(self):
        tema = self.service.state["theme"]
        idioma = self.service.state["language"]

        # 1. Limpieza de estilos
        self.limpiar_estilos_recursivo(self.main)
        
        # 2. Reiniciar paleta (Para arreglar el bug de fondo negro/blanco)
        app = QApplication.instance()
        app.setPalette(app.style().standardPalette())

        # 3. Aplicar Tema
        StyleManager.aplicar_tema(tema)

        # 4. Traducir UI
        self.retraducir_ui(idioma)

        # 5. Sincronizar combos
        self.ui.combo_theme.setCurrentText(tema)
        self.ui.combo_language.setCurrentText(idioma)

    def retraducir_ui(self, idioma):
        """Traduce la interfaz directamente sin chequeos redundantes"""
        t = TRADUCCIONES.get(idioma, TRADUCCIONES["Español"])

        # --- 1. MAIN VIEW (Botones Menú) ---
        self.main.ui.btn_dashboard.setText(t["menu_dash"])
        self.main.ui.btn_reports.setText(t["menu_rep"])
        self.main.ui.btn_settings.setText(t["menu_set"])
        self.main.ui.btn_exit.setText(t["menu_out"])
        
        # --- 2. DASHBOARD VIEW ---
        ui_dash = self.main.ui_dashboard
        ui_dash.label_title.setText(t["dash_title"])
        ui_dash.btn_refresh.setText(t["dash_refresh"])
        
        # Títulos de las cajas (Group Boxes)
        ui_dash.group_score.setTitle(t["dash_top_score"])
        ui_dash.group_active.setTitle(t["dash_top_active"])
        ui_dash.group_jumps.setTitle(t["dash_top_jumps"])

        # Cabeceras de Tablas (Directo, sin IFs)
        # Tabla Score
        ui_dash.table_score.horizontalHeaderItem(0).setText(t["col_player"])
        ui_dash.table_score.horizontalHeaderItem(1).setText(t["col_record"])
            
        # Tabla Activos
        ui_dash.table_active.horizontalHeaderItem(0).setText(t["col_player"])
        ui_dash.table_active.horizontalHeaderItem(1).setText(t["col_games"])
            
        # Tabla Saltos
        ui_dash.table_jumps.horizontalHeaderItem(0).setText(t["col_player"])
        ui_dash.table_jumps.horizontalHeaderItem(1).setText(t["col_jumps"])

        # --- 3. REPORTS VIEW ---
        ui_rep = self.main.ui_reports
        ui_rep.label_title.setText(t["rep_title"])
        ui_rep.btn_generate_pdf.setText(t["rep_btn"])
        
        # Etiquetas de Título (las que acaban en _va)
        ui_rep.lbl_monedas_va.setText(t["rep_coins_lbl"])
        ui_rep.lbl_recordva.setText(t["rep_record_lbl"])
        ui_rep.lbl_partidasva.setText(t["rep_games_lbl"])
        ui_rep.lbl_saltosva.setText(t["rep_jumps_lbl"])

        # --- 4. SETTINGS VIEW ---
        ui_set = self.main.ui_settings
        ui_set.label_title.setText(t["set_title"])
        ui_set.label_theme.setText(t["set_theme_lbl"])
        ui_set.label_lang.setText(t["set_lang_lbl"])

    def limpiar_estilos_recursivo(self, widget):
        widget.setStyleSheet("")
        children = widget.findChildren(QWidget)
        for child in children:
            child.setStyleSheet("")

    def guardar_y_actualizar(self):
        self.service.save(
            self.ui.combo_theme.currentText(),
            self.ui.combo_language.currentText()
        )
        self.aplicar_ajustes_completos()