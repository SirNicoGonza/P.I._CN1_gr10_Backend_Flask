#Controlador de los servidores
from api.datebase import DatabaseConnection
from ..models.servidor_models import Servidor

class ServidorController:
    @classmethod
    def crear_servidor(cls, id_creador, nombre, descripcion):
        # Crear un nuevo servidor en la base de datos
        query = "INSERT INTO servidores (nombre, descripcion) VALUES (%s, %s)"
        params = (nombre, descripcion)

        try:
            cursor = DatabaseConnection.execute_query(query, params)
            id_servidor = cursor.lastrowid
            DatabaseConnection.close_connection()
            query= "INSERT INTO mensajeria.nexo (id_usuario, id_servidor) VALUES(%s,%s);"
            params= (id_creador, id_servidor)
            DatabaseConnection.execute_query(query,params)

            return {"mensaje": "Servidor creado exitosamente", "id_servidor": id_servidor}
        
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
    
    @classmethod
    def obtener_por_id(cls, id_servidor):
        try:
            servidor= Servidor.get_by_id(id_servidor)
            if servidor is not None:
                respuesta= {'id_servidor': id_servidor,
                            'Nombre': servidor['nombre'],
                            'Descripcion': servidor['descripcion'],
                            'creador': servidor['creador']}
                return respuesta
            else:
                return {'error':str('no existe servidor con el id {id_servidor}')}
        except Exception as e:
            return{'error', str(e)}
    
    @classmethod
    def obtener_por_nombre(cls, nombre_servidor):
        try:
            servidor= Servidor.get_by_name(nombre_servidor)
            if servidor is not None:
                respuesta= {'id_servidor': servidor['id'],
                            'Nombre': nombre_servidor,
                            'Descripcion': servidor['descripcion'],
                            'creador': servidor['creador']}
                return respuesta
            else:
                return {'error':str('no existe servidor con el id {nombre_servidor}')}
        except Exception as e:
            return{'error', str(e)}
    
    @classmethod
    def actualizar_nombre(cls, datos):
        try:
            servidor= Servidor.update_name(datos)
            if servidor is not None:
                return {'mensaje':'servidor actualizado'},200
            else:
                return {'Error', 'no se pudo actualizar'}, 500
        except Exception as e:
            return {'Error': str(e)}
    
    @classmethod
    def obtener_todos_canales(cls, id_servidor):
        try:
            canales= Servidor.get_all_canales(id_servidor)
            if canales is not None:
                return canales
            else:
                return None
        except Exception as e:
            return {'Error': str(e)}
    
    @classmethod
    def eliminar_servidor_id(cls, id_servidor):
        try:
            delete= Servidor.delete_servidor(id_servidor)
            #print(delete)
            if delete == True:
                return {'mensaje': 'servidor eliminado'}
            else:
                return {'Error': 'no se pudo eliminar'}
        except:
            return {'Error': 'no se pudo conectar con la base de datos'}, 500
