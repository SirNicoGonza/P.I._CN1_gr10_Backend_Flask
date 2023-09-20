#Controlador de los servidores
from api.datebase import DatabaseConnection
from ..models.servidor_models import Servidor

class ServidorController:
    @classmethod
    def crear_servidor(cls, id_creador, nombre, descripcion):
        # Crear un nuevo servidor en la base de datos
        query = "INSERT INTO servidores (nombre, descripcion, id_creador) VALUES (%s, %s, %s)"
        params = (nombre, descripcion, id_creador)

        try:
            cursor = DatabaseConnection.execute_query(query, params)
            servidor_id = cursor.lastrowid
            DatabaseConnection.close_connection()
            return {"mensaje": "Servidor creado exitosamente", "id_servidor": servidor_id}
        except Exception as e:
            return {"error": str(e)}
    
    @classmethod
    def obtener_servidores(cls):
        # Obtiene todos los servidores
        try:
            servidores= Servidor.get_servidores()
            return servidores
        except Exception as e:
            return {'error', str(e)}
