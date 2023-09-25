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
    @classmethod
    def delete_canal(cls, id_canal):
        try:
            query= "DELETE FROM mensajeria.canales WHERE mensajeria.canales.id=%s;"
            params= (id_canal,)
            DatabaseConnection.execute_query(query,params)
            return True
        
        except Exception as e:
            return {'Error': str(e)}
    
    @classmethod
    def get_mensajes(cls,id_canal):
        try:
            query= """SELECT mensajeria.mensajes.contenido, mensajeria.mensajes.fecha_hora, mensajeria.usuarios.nombre_usuario FROM mensajeria.mensajes
                    INNER JOIN mensajeria.usuarios
                    ON mensajeria.usuarios.id= mensajeria.mensajes.id_remitente
                    INNER JOIN mensajeria.canales
                    ON mensajeria.canales.id= mensajeria.mensajes.id_canal
                    WHERE mensajeria.canales.id=%s
                    GROUP BY mensajeria.mensajes.contenido, mensajeria.mensajes.fecha_hora, mensajeria.usuarios.nombre_usuario
                    ORDER BY mensajeria.mensajes.fecha_hora;"""
            params= (id_canal)
            mensajes= DatabaseConnection.fetch_all(query,params)

            if mensajes is not None:
                return mensajes
            else:
                return None
            
        except Exception as e:
            return {'Error': str(e)}

            
