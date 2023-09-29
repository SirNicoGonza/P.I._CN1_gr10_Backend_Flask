#Controlador de los servidores
from api.datebase import DatabaseConnection

class ServidorController:
    @classmethod
    def crear_servidor(cls, nombre, descripcion):
        # Crear un nuevo servidor en la base de datos
        query = "INSERT INTO servidores (nombre, descripcion) VALUES (%s, %s)"
        params = (nombre, descripcion)

        try:
            cursor = DatabaseConnection.execute_query(query, params)
            servidor_id = cursor.lastrowid
            DatabaseConnection.close_connection()
            return {"mensaje": "Servidor creado exitosamente", "id_servidor": servidor_id}
        except Exception as e:
            return {"error": str(e)}