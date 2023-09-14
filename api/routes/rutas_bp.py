from flask import Blueprint, request, jsonify
from ..controller.user_controller import UsuarioController

# Crear un Blueprint para las rutas relacionadas con usuarios
usuario_bp = Blueprint('usuario', __name__)

# Ruta para registrar un usuario
@usuario_bp.route('/registro', methods=['POST'])
def registro_usuario():
    # Obtener los datos del formulario o del JSON de la solicitud
    datos_registro = request.json
    
    # Crear un objeto Usuario con los datos recibidos
    nuevo_usuario = UsuarioController(
        nombre_usuario=datos_registro.get('nombre_usuario'),
        contraseña=datos_registro.get('contraseña'),
        correo_electronico=datos_registro.get('correo_electronico'),
        imagen_perfil=datos_registro.get('imagen_perfil')
    )
    
    # Llamar al método para crear un usuario en la base de datos
    respuesta = UsuarioController.crear_usuario(nuevo_usuario)
    
    if "error" in respuesta:
        # Si hay un error, responder con un mensaje de error
        return jsonify({"mensaje": "Error al registrar usuario", "error": respuesta["error"]}), 500

    # Si no hay errores, responder con un mensaje de éxito
    return jsonify({"mensaje": "Registro exitoso", "usuario_creado": respuesta["usuario"]}), 200
