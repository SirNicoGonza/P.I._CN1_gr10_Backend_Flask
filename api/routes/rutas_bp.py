from flask import Blueprint, request, jsonify
from ..models.usuario_models import Usuario  
from ..controller.servidor_controller import ServidorController
from ..controller.canal_controller import CanalController
from ..controller.mensaje_controller import MensajeController


# Crear un Blueprint para las rutas relacionadas con usuarios
usuario_bp = Blueprint('usuario', __name__)

# Ruta para registrar un usuario
@usuario_bp.route('/registro', methods=['POST'])
def registro_usuario():
    # Obtener los datos del formulario o del JSON de la solicitud
    #datos_registro = request.json
    datos_registro = request.form
    print("Datos recibidos:", datos_registro)
    # Crear un objeto Usuario con los datos recibidos
    nuevo_usuario = Usuario(
        nombre_usuario=datos_registro.get('nombre_usuario'),
        contraseña=datos_registro.get('contraseña'),
        correo_electronico=datos_registro.get('correo_electronico'),
        imagen_perfil=datos_registro.get('imagen_perfil')
    )
    print("Nuevo usuario creado:", nuevo_usuario)

    # Llamar al método para crear un usuario en la base de datos
    respuesta = Usuario.crear_usuario(nuevo_usuario)  
    print("Respuesta del servidor:", respuesta)
    if "error" in respuesta:
        # Si hay un error, responder con un mensaje de error
        return jsonify({"mensaje": "Error al registrar usuario", "error": respuesta["error"]}), 500

    # Si no hay errores, responder con un mensaje de éxito
    return jsonify({"mensaje": "Registro exitoso", "usuario_creado": respuesta["id_usuario"]}), 200

# Ruta para el inicio de sesión
@usuario_bp.route('/login', methods=['POST'])
def login_usuario():
    # Obtener los datos del formulario o del JSON de la solicitud
    datos_login = request.form
    print("Datos de inicio de sesión recibidos:", datos_login)

    # Buscar al usuario en la base de datos
    nombre_usuario = datos_login.get('username')
    usuario = Usuario.get_usuario_por_nombre(nombre_usuario)

    if isinstance(usuario, dict) and "error" in usuario:
        # Si hay un error, devolver un error
        return jsonify({"mensaje": "Error: " + usuario["error"]}), 500

    if usuario is None:
        # Si el usuario no existe, devolver un error
        return jsonify({"mensaje": "Error: nombre de usuario o contraseña incorrectos"}), 401

    # Comparar la contraseña en texto plano 
    if usuario.contraseña == datos_login.get('password'):
        # Si la contraseña es correcta, devolver una respuesta de éxito
        return jsonify({"mensaje": "Inicio de sesión exitoso"}), 200
    else:
        # Si la contraseña no es correcta, devolver un error
        return jsonify({"mensaje": "Error: nombre de usuario o contraseña incorrectos"}), 401


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