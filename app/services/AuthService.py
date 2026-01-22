import requests
import firebase_admin
from firebase_admin import credentials, db

class AuthService:
    def __init__(self):
        # ================= CONFIGURACIÓN =================
        # 1. Pega aquí tu API KEY WEB (La larga que empieza por AIza...)
        self.api_key = "AIzaSyDTMoade-YjI8ooxj9gqgNcHEup_fHiLf8"
        
        # 2. Pega aquí la URL de tu base de datos (https://... .firebasedatabase.app/)
        self.db_url = "https://cybersprint-tfg-default-rtdb.europe-west1.firebasedatabase.app"
        
        # 3. Nombre del archivo json que descargaste
        self.cred_file = "firebase_key.json"
        # =================================================

        # Iniciamos Firebase solo si no está iniciado ya
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate(self.cred_file)
                firebase_admin.initialize_app(cred, {
                    'databaseURL': self.db_url
                })
                print("Firebase iniciado correctamente.")
            except Exception as e:
                print(f"Error iniciando Firebase: {e}")

        self.current_user_id = None

    def login(self, email, password):
        """
        Envía email y contraseña a Google.
        Devuelve: (True, ID_USUARIO) si sale bien
                  (False, MENSAJE_ERROR) si sale mal
        """
        # Endpoint oficial de Google Identity Toolkit para login con email/pass
        request_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.api_key}"
        
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }

        try:
            # Hacemos la petición web (como si fuera un navegador)
            response = requests.post(request_url, json=payload)
            data = response.json()

            # Verificamos si Google nos dio un error
            if "error" in data:
                mensaje = data["error"]["message"]
                print(f"Error Login: {mensaje}")
                return False, mensaje
            
            # ¡Login correcto! Guardamos el ID
            self.current_user_id = data["localId"]
            return True, self.current_user_id

        except Exception as e:
            print(f"Error de conexión: {e}")
            return False, str(e)

    def obtener_datos_usuario(self):
        """
        Descarga el récord y las monedas del usuario logueado actualmente.
        """
        if self.current_user_id:
            try:
                # Vamos a la carpeta 'jugadores' y buscamos por el ID
                ref = db.reference(f'jugadores/{self.current_user_id}')
                return ref.get()
            except Exception as e:
                print(f"Error leyendo base de datos: {e}")
        return None