# app/services/SettingsService.py
import os
import json

class SettingsService:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.file_path = os.path.join(base_dir, "data", "setting.json")
        self.state = {"theme": "Claro", "language": "Español"}
        self.load()

    def load(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r", encoding="utf-8") as f:
                    self.state.update(json.load(f))
        except Exception as e:
            print(f"Error cargando: {e}")
    
    def save(self, theme, language):
        self.state["theme"] = theme
        self.state["language"] = language
        # CREA LA CARPETA SI NO EXISTE
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=4)