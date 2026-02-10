from PySide6.QtWidgets import QWidget, QTableWidgetItem, QFileDialog, QMessageBox
from PySide6.QtCore import Qt

# Imports
from app.services.report_generator import ReportService
from app.controller.UserDetalleController import UserDetailsController

class PanelController(QWidget):
    def __init__(self, main_controller):
        super().__init__()
        self.main = main_controller
        self.ui = self.main.ui_dashboard
        self.data_service = self.main.data_service

        self.lista_score = []
        self.lista_active = []
        self.lista_jumps = []

        self.ui.btnTOPPuntuacion.clicked.connect(self.exportar_score)
        self.ui.btnTOPActivos.clicked.connect(self.exportar_active)
        self.ui.btnTOPSaltos.clicked.connect(self.exportar_jumps)

        self.ui.btn_refresh.clicked.connect(self.cargar_tablas)

        self.ui.table_score.cellDoubleClicked.connect(self.al_doble_clic_score)
        self.ui.table_active.cellDoubleClicked.connect(self.al_doble_clic_active)
        self.ui.table_jumps.cellDoubleClicked.connect(self.al_doble_clic_jumps)
        
        self.cargar_tablas()

    def cargar_tablas(self):
        self.lista_score = self.data_service.obtener_ranking('record')
        self.lista_active = self.data_service.obtener_ranking('partidas_totales')
        self.lista_jumps = self.data_service.obtener_ranking('saltos_totales')

        self.rellenar_widget(self.ui.table_score, self.lista_score)
        self.rellenar_widget(self.ui.table_active, self.lista_active)
        self.rellenar_widget(self.ui.table_jumps, self.lista_jumps)

    def rellenar_widget(self, tabla, filas):
        tabla.setRowCount(0)
        tabla.setRowCount(len(filas))
        for i, d in enumerate(filas):
            item_nombre = QTableWidgetItem(str(d["nombre"]))
            item_nombre.setData(Qt.UserRole, d) 
            tabla.setItem(i, 0, item_nombre)

            val = QTableWidgetItem(str(d["valor"]))
            val.setTextAlignment(Qt.AlignCenter)
            tabla.setItem(i, 1, val)

    def al_doble_clic_score(self, row, col):
        self.abrir_popup(self.ui.table_score, row)

    def al_doble_clic_active(self, row, col):
        self.abrir_popup(self.ui.table_active, row)

    def al_doble_clic_jumps(self, row, col):
        self.abrir_popup(self.ui.table_jumps, row)

    def abrir_popup(self, tabla, fila):
        """Lógica común para abrir la ventana"""
        item = tabla.item(fila, 0)
        if item:
            datos = item.data(Qt.UserRole)
            popup = UserDetailsController(datos, self.main)
            popup.exec()

    def exportar_score(self):
        self._generar_pdf("Ranking_Puntuacion.pdf", "Récord de Puntuación", "Puntos", self.lista_score)

    def exportar_active(self):
        self._generar_pdf("Ranking_Actividad.pdf", "Jugadores Más Activos", "Partidas", self.lista_active)

    def exportar_jumps(self):
        self._generar_pdf("Ranking_Saltos.pdf", "Saltos Totales", "Saltos", self.lista_jumps)

    def _generar_pdf(self, default_name, titulo, col_name, datos):
        if not datos:
            QMessageBox.warning(self.main, "Aviso", "No hay datos para exportar.")
            return

        path, _ = QFileDialog.getSaveFileName(self.main, "Guardar Ranking PDF", default_name, "Archivos PDF (*.pdf)")
        if path:
            try:
                ReportService.generar_informe_ranking(path, titulo, col_name, datos)
                QMessageBox.information(self.main, "Éxito", "Ranking exportado correctamente.")
            except Exception as e:
                QMessageBox.critical(self.main, "Error", f"No se pudo generar el PDF:\n{e}")