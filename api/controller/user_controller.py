from api.datebase import DatabaseConnection

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
    def crear_usuario(cls, nombre, correo_electronico, contraseña):
        # Crear un nuevo usuario en la base de datos
        query = "INSERT INTO usuarios (nombre_usuario, correo_electronico, contraseña) VALUES (%s, %s, %s)"
        params = (nombre, correo_electronico, contraseña)

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
        query = "SELECT * FROM usuarios WHERE id = %s"
        params = (id_usuario,)

        try:
            cursor = DatabaseConnection.execute_query(query, params)
            usuario_info = cursor.fetchone()
            DatabaseConnection.close_connection()
            
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
