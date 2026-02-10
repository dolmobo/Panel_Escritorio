import requests
import firebase_admin
from firebase_admin import credentials, db
import os

class AuthService:
    def __init__(self):
        # Asegúrate de que tu API KEY es correcta
        self.api_key = "AIzaSyDTMoade-YjI8ooxj9gqgNcHEup_fHiLf8"
        self.db_url = "https://cybersprint-tfg-default-rtdb.europe-west1.firebasedatabase.app"
        
        # Ruta dinámica al archivo de credenciales para evitar errores de ruta
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.cred_file = os.path.join(base_dir, "serviceAccountKey.json")
        
        if not firebase_admin._apps:
            try:
                if os.path.exists(self.cred_file):
                    cred = credentials.Certificate(self.cred_file)
                    firebase_admin.initialize_app(cred, {
                        'databaseURL': self.db_url
                    })
                    print("Firebase iniciado correctamente.")
                else:
                    print(f"Error: No se encuentra el archivo {self.cred_file}")
            except Exception as e:
                print(f"Error iniciando Firebase: {e}")

        self.current_user_id = None

    def login(self, email, password):
        """
        Envía email y contraseña a Google.
        Devuelve: (UID, NOMBRE_USUARIO) si sale bien <-- CAMBIO IMPORTANTE
                  (False, MENSAJE_ERROR) si sale mal
        """
        request_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.api_key}"
        
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }

        try:
            response = requests.post(request_url, json=payload)
            data = response.json()

            if "error" in data:
                mensaje = data["error"]["message"]
                print(f"Error Login: {mensaje}")
                return False, mensaje
            
            # Guardamos el ID interno de Firebase
            self.current_user_id = data["localId"]
            
            # Parseamos el nombre del email
            username = email.split('@')[0]
            username_bonito = username.capitalize()
            
            return self.current_user_id, username_bonito

        except Exception as e:
            print(f"Error de conexión: {e}")
            return False, str(e)