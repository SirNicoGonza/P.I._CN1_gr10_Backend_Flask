from api.datebase import DatabaseConnection


class Usuario():
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.nombre_usuario = kwargs.get('nombre_usuario')
        self.contraseña = kwargs.get('contraseña')
        self.correo_electronico = kwargs.get('correo_electronico')
        self.imagen_perfil = kwargs.get('imagen_perfil')
        self.amigos = []  # Lista de amigos
        self.servidores = []  # Lista de servidores a los que pertenece
        self.is_active = True  # Añadir un atributo is_active
        
    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

    def unirse_a_servidor(self, servidor):
        self.servidores.append(servidor)
   
   
    @classmethod
    def crear_usuario(cls, usuario):
        """Crea un nuevo usuario"""
        query = """INSERT INTO mensajeria.usuarios (nombre_usuario, contraseña, correo_electronico, imagen_perfil) VALUES (%s, %s, %s, %s)"""
        params = (usuario.nombre_usuario, usuario.contraseña, usuario.correo_electronico, usuario.imagen_perfil)

        # Imprimir la consulta SQL completa
        # print("Query: ", query)
        # print("Params: ", params)

        try:
            cursor = DatabaseConnection.execute_query(query, params)
            id_usuario = cursor.lastrowid
            DatabaseConnection.close_connection()
            return {"mensaje": "Usuario creado exitosamente", "id_usuario": id_usuario}
        except Exception as e:
            # print("Error executing query: ", e)
            return {"error": str(e)}

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_usuario': self.nombre_usuario,
            'contraseña': self.contraseña,
            'correo_electronico': self.correo_electronico,
            'imagen_perfil': self.imagen_perfil
        }
    
    @classmethod
    def get_usuario_por_nombre(cls, nombre_usuario):
        """Método para traer la información de un usuario por su nombre de usuario."""
        query = """SELECT id, contraseña, correo_electronico, imagen_perfil FROM mensajeria.usuarios WHERE nombre_usuario = %s;"""
        params = (nombre_usuario,)

        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, params)
            
            resultado = cursor.fetchone()
            
            if resultado is not None:
                id_usuario, contraseña, correo_electronico, imagen_perfil = resultado
                    
                # Crea una instancia de Usuario con los datos obtenidos
                usuario = Usuario(
                    id=id_usuario,
                    nombre_usuario=nombre_usuario,
                    contraseña=contraseña,
                    correo_electronico=correo_electronico,
                    imagen_perfil=imagen_perfil
                )
                
                return usuario
            else:
                print("Usuario no encontrado en la base de datos")
                return None  # El usuario no existe
        except Exception as e:
            print("Error executing query: ", e)
            return None  
        finally:
            if cursor:
                cursor.close()


   