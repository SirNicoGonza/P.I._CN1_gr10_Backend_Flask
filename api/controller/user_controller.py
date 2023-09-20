from api.datebase import DatabaseConnection
from ..models.usuario_models import Usuario

class UsuarioController:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.nombre_usuario = kwargs.get('nombre_usuario')
        self.contraseña = kwargs.get('contraseña')
        self.correo_electronico = kwargs.get('correo_electronico')
        self.imagen_perfil = kwargs.get('imagen_perfil')
        self.amigos = []  # Lista de amigos
        self.servidores = []  # Lista de servidores a los que pertenece

    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

    def unirse_a_servidor(self, servidor):
        self.servidores.append(servidor)

    @classmethod
    def crear_usuario(cls, usuario):
        # Crear un nuevo usuario en la base de datos
        query = "INSERT INTO usuarios (nombre_usuario, contraseña, correo_electronico, imagen_perfil) VALUES (%s, %s, %s, %s)"
        params = (usuario.nombre_usuario, usuario.contraseña, usuario.correo_electronico, usuario.imagen_perfil)

        try:
            cursor = DatabaseConnection.execute_query(query, params)
            usuario_id = cursor.lastrowid
            DatabaseConnection.close_connection()
            return {"mensaje": "Usuario creado exitosamente", "id_usuario": usuario_id}
        except Exception as e:
            return {"error": str(e)}


    @classmethod
    def obtener_usuario_por_id(cls, id_usuario):
        # Obtener información de un usuario por su ID
        try:
            usuario_info= Usuario.get_usuario(id_usuario)
            
            if usuario_info:
                usuario = cls(
                    id=usuario_info[0],
                    nombre_usuario=usuario_info[1],
                    correo_electronico=usuario_info[2],
                    contraseña=usuario_info[3],
                    imagen_perfil=usuario_info[4]
                )
                return {"usuario": usuario.__dict__}
            else:
                return {"mensaje": "Usuario no encontrado"}
        except Exception as e:
            return {"error": str(e)}
    
    @classmethod
    def actualizar_usuario_por_id(cls, datos):
        # Para actualizar el nombre y la contraseña del usuario
        try:
            usuario= Usuario.update_usuario(datos)
            if usuario is not None:
                return {'mensaje': usuario}, 200
            else:
                return {'mensaje': 'usuario no encotrado'}, 200
        except Exception as e:
            return {'Error': str(e)}