from api.datebase import DatabaseConnection

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
    
    @classmethod
    def serializar(cls, lista):
        dicc={
            'id': lista[0],
            'nombre': lista[1],
            'descripcion': lista[2],
            'creador': lista[3]
        }
        return dicc

    @classmethod
    def get_servidores(cls):
        try:
            query= "SELECT nombre, descripcion FROM mensajeria.servidores;"
            resultado= DatabaseConnection.fetch_all(query)
            return resultado
        except Exception as e:
            return {'Error':str(e)}, 500
    
    @classmethod
    def get_by_id(cls,id_servidor):
        try:
            query= """SELECT se.id, se.nombre, se.descripcion, us.nombre_usuario FROM servidores se
                    INNER JOIN usuarios us
                    ON us.id = se.id_creador
                    WHERE se.id= %s
                    GROUP BY se.id, se.nombre, se.descripcion, us.nombre_usuario
                    ORDER BY se.nombre;"""
            params= id_servidor
            resultado= DatabaseConnection.fetch_one(query,(params))

            if resultado is not None:
                return Servidor.serializar(resultado)
            else:
                return None
        except Exception as e:
            return {'Error': str(e)}

    @classmethod
    def get_by_name(cls,nombre_servidor):
        try:
            query= """SELECT se.id, se.nombre, se.descripcion, us.nombre_usuario FROM servidores se
                    INNER JOIN usuarios us
                    ON us.id = se.id_creador
                    WHERE se.nombre= %s
                    GROUP BY se.id, se.nombre, se.descripcion, us.nombre_usuario
                    ORDER BY se.nombre;"""
            params= nombre_servidor
            resultado= DatabaseConnection.fetch_one(query,(params))

            if resultado is not None:
                return Servidor.serializar(resultado)
            else:
                return None
        except Exception as e:
            return {'Error': str(e)}
