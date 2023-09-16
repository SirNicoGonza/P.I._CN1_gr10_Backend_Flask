from flask import Blueprint, request, jsonify
from ..models.usuario_models import Usuario  
from ..controller.servidor_controller import ServidorController


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