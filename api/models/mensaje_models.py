# mensaje_models.py
from api.datebase import DatabaseConnection

class Mensaje:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.contenido = kwargs.get('contenido')
        self.fecha_hora = kwargs.get('fecha_hora')
        self.id_canal = kwargs.get('id_canal')
        self.id_remitente = kwargs.get('id_remitente')

    def __str__(self):
        return f"{self.fecha_hora}: {self.id_remitente} - {self.contenido}"
    
    @classmethod
    def update_mensaje(cls,id_mensaje,mensaje_new):
        try:
            query= "UPDATE mensajeria.mensajes SET contenido=%s WHERE id=%s;"
            params= (mensaje_new, id_mensaje)
            DatabaseConnection.execute_query(query,params)
            return str("update"), 200
        except Exception as e:
            print(f"Error = {e}")
            return None, 500
    
    @classmethod
    def delete_mensaje(cls,id_mensaje):
        try:
            query= "DELETE FROM mensajeria.mensajes WHERE mensajeria.mensajes.id=%s;"
            params= (id_mensaje,)
            DatabaseConnection.execute_query(query,params)
            return True
        
        except Exception as e:
            return {'Error': str(e)}