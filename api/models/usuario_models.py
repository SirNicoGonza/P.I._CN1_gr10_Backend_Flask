from api.datebase import DatabaseConnection

class Usuario:
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
        """Crea un nuevo usuario"""
        query = """INSERT INTO mensajeria.usuarios (nombre_usuario, contraseña, correo_electronico, imagen_perfil) VALUES (%s, %s, %s, %s)"""
        params = (usuario.nombre_usuario, usuario.contraseña, usuario.correo_electronico, usuario.imagen_perfil)

        # Imprimir la consulta SQL completa
        print("Query: ", query)
        print("Params: ", params)

        try:
            cursor = DatabaseConnection.execute_query(query, params)
            id_usuario = cursor.lastrowid
            DatabaseConnection.close_connection()
            return {"mensaje": "Usuario creado exitosamente", "id_usuario": id_usuario}
        except Exception as e:
            print("Error executing query: ", e)
            return {"error": str(e)}


    
    @classmethod
    def get_usuario(cls, id_usuario):
        """ Método para traer la información de un usuario. """
        query = """SELECT * FROM mensajeria.usuarios WHERE id= %s;"""
        params = id_usuario
        resultado = DatabaseConnection.fetch_one(query, params)
        DatabaseConnection.close_connection()
        if resultado is not None:
            return resultado
        else:
            return {'Mensaje': 'El cliente no existe'}  # Luego lo cambiamos por el manejo de errores
