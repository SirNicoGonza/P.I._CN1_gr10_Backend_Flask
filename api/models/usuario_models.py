## Tendria que ir la coneccion a la base de datos
from ..datebase import DatabaseConnection

class Usuario:
    def _init_(self, **kwargs):
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
    def crear_usuario(cls,usuario):
        """Crea un nuevo usuario"""
        query= """INSERT INTO mensajeria.usuarios (nombre_usuario, contraseña, correo_electronico, imagen_perfil) VALUES (%s, %s, %s, %s);"""
        params= (usuario.nombre_usuario, usuario.contraseña, usuario.correo_electronico, usuario.imagen_perfil)
        DatabaseConnection.execute_query(query,params)
        DatabaseConnection.close_connection()
    
    @classmethod
    def get_usuario(cls, id_usuario):
        """ Metodo para traer la informacion de un usuario. """
        query= """SELECT nombre_usuario, contraseña, correo_electronico, imagen_perfil FROM mensajeria.usuarios WHERE id = %s;"""
        params= id_usuario
        resultado= DatabaseConnection.fetch_one(query, params)
        DatabaseConnection.close_connection()
        if resultado is not None:
            aux= Usuario(id= id_usuario,
                        nombre_usuario= resultado[0], 
                        contraseña= resultado[1],
                        correo_electronico= resultado[2],
                        imagen_perfil= resultado[3] 
                        )
            return aux.__dict__
            
        
        else:
            return {'Mensaje': 'El cliente no existe'} # Luego lo cambiamos por el manejo de errore s
