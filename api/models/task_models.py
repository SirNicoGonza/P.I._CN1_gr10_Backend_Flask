##
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


class Servidor:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.nombre = kwargs.get('nombre')
        self.descripcion = kwargs.get('descripcion')
        self.id_creador = kwargs.get('id_creador')
        self.canales = []  # Lista de canales dentro del servidor
        self.miembros = []  # Lista de miembros (usuarios) del servidor

    def agregar_canal(self, canal):
        self.canales.append(canal)

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)


class Canal:
    def _init_(self, **kwargs):
        self.id = kwargs.get('id')
        self.nombre = kwargs.get('nombre')
        self.id_servidor = kwargs.get('id_servidor')
        self.id_creador = kwargs.get('id_creador')
        self.mensajes = []  # Lista de mensajes en el canal

    def enviar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)


class Mensaje:
    def _init_(self, **kwargs):
        self.id = kwargs.get('id')
        self.contenido = kwargs.get('contenido')
        self.fecha_hora = kwargs.get('fecha_hora')
        self.id_canal = kwargs.get('id_canal')
        self.id_remitente = kwargs.get('id_remitente')

    def _str_(self):
        return f"{self.fecha_hora}: {self.id_remitente} - {self.contenido}"
    
class Category:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.nombre = kwargs.get('nombre')    