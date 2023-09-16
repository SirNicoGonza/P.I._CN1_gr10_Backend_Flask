

# mensaje_controller.py
from api.datebase import DatabaseConnection

class MensajeController:
    @classmethod
    def conseguir_mensajes(cls, id_canal):
        # Implementa la lógica para obtener todos los mensajes de un canal específico
        query = "SELECT * FROM mensajes WHERE id_canal = %s"
        params = (id_canal,)
        
        try:
            # Ejecuta la consulta y obtén los mensajes
            mensajes = DatabaseConnection.fetch_all(query, params)
            return mensajes
        except Exception as e:
            return {"error": str(e)}

    @classmethod
    def enviar_mensaje(cls, contenido, id_canal, id_remitente):
        # Implementa la lógica para enviar un mensaje a un canal específico
        query = "INSERT INTO mensajes (contenido, id_canal, id_remitente) VALUES (%s, %s, %s)"
        params = (contenido, id_canal, id_remitente)
        
        try:
            # Ejecuta la consulta para enviar el mensaje
            cursor = DatabaseConnection.execute_query(query, params)
            mensaje_id = cursor.lastrowid
            DatabaseConnection.close_connection()
            return {"mensaje": "Mensaje enviado exitosamente", "id_mensaje": mensaje_id}
        except Exception as e:
            return {"error": str(e)}