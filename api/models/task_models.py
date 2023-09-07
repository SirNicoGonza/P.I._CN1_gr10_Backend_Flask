##
class Usuario:
    def _init_(self, id, nombre_usuario, contraseña, correo_electronico, imagen_perfil):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.correo_electronico = correo_electronico
        self.imagen_perfil = imagen_perfil
        self.amigos = []  # Lista de amigos
        self.servidores = []  # Lista de servidores a los que pertenece

    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

    def unirse_a_servidor(self, servidor):
        self.servidores.append(servidor)


class Servidor:
    def _init_(self, id, nombre, descripcion, id_creador):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_creador = id_creador
        self.canales = []  # Lista de canales dentro del servidor
        self.miembros = []  # Lista de miembros (usuarios) del servidor

    def agregar_canal(self, canal):
        self.canales.append(canal)

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)


class Canal:
    def _init_(self, id, nombre, id_servidor, id_creador):
        self.id = id
        self.nombre = nombre
        self.id_servidor = id_servidor
        self.id_creador = id_creador
        self.mensajes = []  # Lista de mensajes en el canal

    def enviar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)


class Mensaje:
    def _init_(self, id, contenido, fecha_hora, id_canal, id_remitente):
        self.id = id
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.id_canal = id_canal
        self.id_remitente = id_remitente

    def _str_(self):
        return f"{self.fecha_hora}: {self.id_remitente} - {self.contenido}"