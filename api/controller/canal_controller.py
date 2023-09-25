#Controladro de los canales
from api.datebase import DatabaseConnection
from ..models.canal_models import Canal

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
            return {"error": str(e)}

    @classmethod
    def actualizar_nombre(cls,datos):
        try:
            servidor= Canal.update_name(datos)
            if servidor is not None:
                return {'mensaje':'servidor actualizado'},200
            else:
                return {'Error', 'no se pudo actualizar'}, 500
        except Exception as e:
            return {'Error': str(e)}
    
    @classmethod
    def eliminar_canal_id(cls,id_canal):
        try:
            delete= Canal.delete_canal(id_canal)
            #print(delete)
            if delete == True:
                return {'mensaje': 'canal eliminado'}
            else:
                return {'Error': 'no se pudo eliminar'}
        except:
            return {'Error': 'no se pudo conectar con la base de datos'}, 500
    
    @classmethod
    def traer_mensajes_by_id(cls,id_canal):
        try:
            mensajes= Canal.get_mensajes(id_canal)
            if mensajes:
                return mensajes
            else:
                return None
        except Exception as e:
            return {'Error': str(e)}
    
 #   def _init_(self, **kwargs):
 #       self.id = kwargs.get('id')
 #       self.nombre = kwargs.get('nombre')
 #       self.id_servidor = kwargs.get('id_servidor')
 #       self.id_creador = kwargs.get('id_creador')
 #       self.mensajes = []  # Lista de mensajes en el canal

 #   def enviar_mensaje(self, mensaje):
 #      self.mensajes.append(mensaje)