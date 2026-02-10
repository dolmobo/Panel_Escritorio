# Modificación en app/styles/StyleManager.py
import os
from PySide6.QtWidgets import QApplication

class StyleManager:
    def aplicar_tema(nombre_tema):
        tema = "claro" if "claro" in nombre_tema.lower() else "oscuro"
        archivo = f"{tema}.qss"
        
        ruta_base = os.path.dirname(os.path.abspath(__file__))
        ruta_completa = os.path.join(ruta_base, archivo)

        if os.path.exists(ruta_completa):
            with open(ruta_completa, "r", encoding="utf-8") as f:
                estilo = f.read()
                app = QApplication.instance()
                # IMPORTANTE: Forzar la limpieza y re-aplicación
                app.setStyleSheet("") 
                app.setStyleSheet(estilo)
                # Opcional: Forzar a que todos los widgets se repinten
                for widget in app.allWidgets():
                    # Accedemos al objeto QStyle que maneja el widget
                    estilo_del_widget = widget.style() 
                    
                    # Llamamos a los métodos pasando el widget como argumento
                    estilo_del_widget.unpolish(widget)
                    estilo_del_widget.polish(widget)
                    
                    # Forzamos el redibujado
                    widget.update()