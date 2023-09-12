#Controladro de los mensajes

class MensajeController:
    ###Aqui definimos los metodos de clase
    
    def _init_(self, **kwargs):
        self.id = kwargs.get('id')
        self.contenido = kwargs.get('contenido')
        self.fecha_hora = kwargs.get('fecha_hora')
        self.id_canal = kwargs.get('id_canal')
        self.id_remitente = kwargs.get('id_remitente')

    def _str_(self):
        return f"{self.fecha_hora}: {self.id_remitente} - {self.contenido}"