#Aqui van las Los blueprints

from flask import Blueprint, request, jsonify
from api.datebase import DatabaseConnection


# Crear un Blueprint 
auth_bp = Blueprint('auth', __name__)

# Ruta de registro de usuarios
@auth_bp.route('/registro', methods=['POST'])
def registro_usuario():
    # Obtiene los datos del formulario o del JSON de la solicitud
    datos_registro = request.json 

    # Extrae los campos del formulario o JSON
    nombre_usuario = datos_registro.get('nombre_usuario')
    contraseña = datos_registro.get('contraseña')
    correo_electronico = datos_registro.get('correo_electronico')

    # Validar los datos 
    

    
    respuesta = {
        'mensaje': 'Registro exitoso',
        'usuario_creado': {
            'nombre_usuario': nombre_usuario,
            'correo_electronico': correo_electronico
        }
    }
    return jsonify(respuesta), 200
