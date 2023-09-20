from flask import Blueprint, request, jsonify
from ..models.usuario_models import Usuario
from ..controller.user_controller import UsuarioController  
from ..controller.servidor_controller import ServidorController
from ..controller.canal_controller import CanalController
from ..controller.mensaje_controller import MensajeController

# Crear un Blueprint para las rutas relacionadas con usuarios
usuario_bp = Blueprint('usuario', __name__)

# Ruta para registrar un usuario
@usuario_bp.route('/registro', methods=['POST'])
def registro_usuario():
    # Obtener los datos del formulario o del JSON de la solicitud
    datos_registro = request.json
    
    # Crear un objeto Usuario con los datos recibidos
    nuevo_usuario = Usuario(
        nombre_usuario=datos_registro.get('nombre_usuario'),
        contraseña=datos_registro.get('contraseña'),
        correo_electronico=datos_registro.get('correo_electronico'),
        imagen_perfil=datos_registro.get('imagen_perfil')
    )
    
    # Llamar al método para crear un usuario en la base de datos
    respuesta = Usuario.crear_usuario(nuevo_usuario)  

    if "error" in respuesta:
        # Si hay un error, responder con un mensaje de error
        return jsonify({"mensaje": "Error al registrar usuario", "error": respuesta["error"]}), 500

    # Si no hay errores, responder con un mensaje de éxito
    return jsonify({"mensaje": "Registro exitoso", "usuario_creado": respuesta["id_usuario"]}), 200

@usuario_bp.route('/get_usuario/<int:id_usuario>', methods= ['GET'])
def obtener_usuario(id_usuario):
    """ Metodo para obtener la info de un usuario"""
    try:
        user= UsuarioController.obtener_usuario_por_id(id_usuario)
        return user, 200
    except:
        return {"error": "no se encontro la pagina"}, 400
    
@usuario_bp.route('/actualizar_usuario/<int:id_usuario>', methods= ['PUT'])
def actualizar_usuario(id_usuario):
    """Metodo para acutalizar el nombre y la contraseña del usuario con la id = 'id_usurio'."""
    try:
        registro= request.json
        datos= registro.get('nombre'), registro.get('contraseña'), id_usuario
        UsuarioController.actualizar_usuario_por_id(datos)
        return {'mensaje':'Datos del usuario se acutalizaron con exito'}, 200
    except:
        return {'error':'no se encontro la pagina ...'}, 400

@usuario_bp.route('/crear_servidor', methods=['POST'])
def crear_servidor():
    datos_servidor = request.json
    nombre = datos_servidor.get('nombre')
    descripcion = datos_servidor.get('descripcion')
    id_creador = datos_servidor.get('id_creador')  #  el ID del usuario que crea el servidor

    respuesta = ServidorController.crear_servidor(id_creador, nombre, descripcion)

    if "error" in respuesta:
        return jsonify({"mensaje": "Error al crear el servidor", "error": respuesta["error"]}), 500

    return jsonify({"mensaje": "Servidor creado exitosamente", "id_servidor": respuesta["id_servidor"]}), 200


@usuario_bp.route('/crear_canal', methods=['POST'])
def crear_canal():
    datos_canal = request.json
    nombre = datos_canal.get('nombre')
    id_servidor = datos_canal.get('id_servidor')
    id_creador = datos_canal.get('id_creador')  # ID del usuario que crea el canal

    respuesta = CanalController.crear_canal(nombre, id_servidor, id_creador)

    if "error" in respuesta:
        return jsonify({"mensaje": "Error al crear el canal", "error": respuesta["error"]}), 500

    return jsonify({"mensaje": "Canal creado exitosamente", "id_canal": respuesta["id_canal"]}), 200

@usuario_bp.route('/enviar_mensaje', methods=['POST'])
def enviar_mensaje():
    datos_mensaje = request.json
    contenido = datos_mensaje.get('contenido')
    id_canal = datos_mensaje.get('id_canal')
    id_remitente = datos_mensaje.get('id_remitente')  # El ID del usuario que envía el mensaje

    respuesta = MensajeController.enviar_mensaje(contenido, id_canal, id_remitente)

    if "error" in respuesta:
        return jsonify({"mensaje": "Error al enviar el mensaje", "error": respuesta["error"]}), 500

    return jsonify({"mensaje": "Mensaje enviado exitosamente", "id_mensaje": respuesta["id_mensaje"]}), 200

@usuario_bp.route('/obtener_mensajes/<int:id_canal>', methods=['GET'])
def obtener_mensajes(id_canal):
    mensajes = MensajeController.conseguir_mensajes(id_canal)

    if "error" in mensajes:
        return jsonify({"mensaje": "Error al obtener mensajes", "error": mensajes["error"]}), 500

    return jsonify({"mensajes": mensajes}), 200