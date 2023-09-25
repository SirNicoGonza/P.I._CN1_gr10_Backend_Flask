# Modelo de canal
from api.datebase import DatabaseConnection

class Canal:
    def _init_(self, **kwargs):
        self.id = kwargs.get('id')
        self.nombre = kwargs.get('nombre')
        self.id_servidor = kwargs.get('id_servidor')
        self.id_creador = kwargs.get('id_creador')
        self.mensajes = []  # Lista de mensajes en el canal

    def enviar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    @classmethod
    def update_name(cls,datos):
        try:
            query= "UPDATE mensajeria.canales SET nombre=%s WHERE id=%s;"
            params= (datos[0], datos[1])
            DatabaseConnection.execute_query(query,params)
            return str("Exito al actualizar"), 200
        except Exception as e:
            return {'Error': str(e)}
