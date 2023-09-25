# Controlador de los canales
from api.datebase import DatabaseConnection

class CanalController:

    @classmethod
    def crear_canal(cls, nombre, id_servidor, id_usuario):
        # Crea un nuevo canal en la base de datos
        query = "INSERT INTO canales (nombre, id_servidor, id_creador) VALUES (%s, %s, %s)"
        params = (nombre, id_servidor, id_usuario)

        try:
            cursor = DatabaseConnection.execute_query(query, params)
            canal_id = cursor.lastrowid
            DatabaseConnection.close_connection()
            return {"mensaje": "Canal creado exitosamente", "id_canal": canal_id}
        except Exception as e:
            print("Error al crear el canal:", str(e))
            return {"error": str(e)}

    @classmethod
    def obtener_canales_por_servidor(cls, id_servidor):
        # Obtiene los canales correspondientes a un servidor desde la base de datos
        query = "SELECT id, nombre FROM canales WHERE id_servidor = %s"
        params = (id_servidor,)

        try:
            cursor = DatabaseConnection.execute_query(query, params)
            canales = []
            for row in cursor.fetchall():
                canal = {
                    "id": row[0],  # Cambiar "id_canal" a "id"
                    "nombre": row[1]
                }
                canales.append(canal)

            # Cierra el cursor antes de cerrar la conexión
            cursor.close()
            
            # Asegúrate de cerrar la conexión después de obtener los resultados
            DatabaseConnection.close_connection()

            # Si no se encontraron canales, devuelve un mensaje específico
            if not canales:
                return {"mensaje": "No se encontraron canales para este servidor"}

            print("Canales obtenidos con éxito:", canales)  # Mensaje de éxito
            return canales
        except Exception as e:
            print("Error al obtener canales:", str(e))  # Mensaje de error
            return {"error": str(e)}
