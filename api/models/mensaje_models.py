# mensaje_models.py
from api.datebase import DatabaseConnection

class Mensaje:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.contenido = kwargs.get('contenido')
        self.fecha_hora = kwargs.get('fecha_hora')
        self.id_canal = kwargs.get('id_canal')
        self.id_remitente = kwargs.get('id_remitente')

    def __str__(self):
        return f"{self.fecha_hora}: {self.id_remitente} - {self.contenido}"