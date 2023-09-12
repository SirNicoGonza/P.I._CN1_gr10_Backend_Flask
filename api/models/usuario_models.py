## Tendria que ir la coneccion a la base de datos
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
    