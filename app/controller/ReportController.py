from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from translations import TRADUCCIONES
from app.services.SettingsService import SettingsService
from app.views.ReportView_ui import Ui_ReportsView
from app.services.report_generator import ReportService

class ReportController(QWidget):
    def __init__(self, main_controller):
        super().__init__()
        self.main = main_controller
        self.ui = self.main.ui_reports
        
        # Conexiones
        self.ui.btn_generate_pdf.clicked.connect(self.lanzar_informe)

    def actualizar_datos(self):
        """
        Método CRUCIAL: Se llama desde MainController al entrar en la pestaña.
        Actualiza los contadores visuales (monedas, récord, etc.)
        """
        # 1. Pedimos los datos frescos a la base de datos
        datos = self.main.data_service.obtener_usuario_por_id(self.main.user_id)
        
        if datos:
            # 2. Actualizamos las etiquetas de la interfaz
            # Usamos .get(..., 0) para evitar errores si el campo no existe
            self.ui.lbl_monedas.setText(str(datos.get('monedas', 0)))
            self.ui.lbl_record.setText(str(datos.get('record', 0)))
            self.ui.lbl_partidas.setText(str(datos.get('partidas_totales', 0)))
            self.ui.lbl_saltos.setText(str(datos.get('saltos_totales', 0)))

    def lanzar_informe(self):
        """Genera el PDF con gráficos"""
        # 1. Obtenemos datos del usuario actual
        datos_usuario = self.main.data_service.obtener_usuario_por_id(self.main.user_id)
        
        settings = SettingsService()
        current_lang = settings.state.get("language", "Español")
        t = TRADUCCIONES.get(current_lang, TRADUCCIONES["Español"])
        
        if not datos_usuario:
            QMessageBox.warning(self.main, t["error_title"], t["user_data_error"])
            return

        # 2. Obtenemos los promedios globales para la comparativa
        promedios = self.main.data_service.obtener_promedios_globales()

        # 3. Preguntamos dónde guardar el PDF
        path, _ = QFileDialog.getSaveFileName(
            self.main, 
            "Guardar Informe PDF", 
            f"Informe_{self.main.user_name}.pdf", 
            "Archivos PDF (*.pdf)"
        )

        if path:
            try:
                # 4. Pasamos todo al generador
                ReportService.generar_informe_perfil(path, datos_usuario, promedios)
                QMessageBox.information(self.main, t["success_title"], t["report_success"])
            except Exception as e:
                QMessageBox.critical(self.main, t["error_title"], t["report_error"].format(error=str(e)))