# app/services/DataService.py
from firebase_admin import db

class DataService:
    def __init__(self):
        self.ref = db.reference('jugadores')

    def obtener_usuario_por_id(self, uid):
        """Trae los datos de un solo jugador usando su UID"""
        try:
            return self.ref.child(uid).get()
        except Exception as e:
            print(f"Error al recuperar usuario: {e}")
            return None

    def obtener_ranking(self, criterio):
        datos = self.ref.get() or {}
        lista = []
        for uid, info in datos.items():
            usuario_completo = info.copy() 
            usuario_completo['nombre'] = str(info.get('username', uid)).split('@')[0].capitalize()
            usuario_completo['valor'] = info.get(criterio, 0)
            lista.append(usuario_completo)
        
        # Ordenar de mayor a menor
        lista.sort(key=lambda e: e['valor'], reverse=True)
        return lista
    
    def obtener_promedios_globales(self):
        """Calcula la media de estadísticas de todos los jugadores de forma eficiente"""
        try:
            usuarios = self.ref.get() or {}
            
            if not usuarios: 
                return None
            
            lista_datos = list(usuarios.values())
            total_usuarios = len(lista_datos)
            
            return {
                'monedas': sum(u.get('monedas', 0) for u in lista_datos) // total_usuarios,
                'record': sum(u.get('record', 0) for u in lista_datos) // total_usuarios,
                'partidas_totales': sum(u.get('partidas_totales', 0) for u in lista_datos) // total_usuarios,
                'saltos_totales': sum(u.get('saltos_totales', 0) for u in lista_datos) // total_usuarios
            }
            
        except Exception as e:
            print(f"Error calculando promedios: {e}")
            return None