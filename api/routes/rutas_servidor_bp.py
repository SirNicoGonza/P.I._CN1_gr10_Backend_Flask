from flask import Blueprint, request, jsonify

from ..controller.servidor_controller import ServidorController

# Crear un Blueprint para las rutas relacionadas con servidores
servidor_bp= Blueprint('servidor',__name__)

# Rutas

@servidor_bp.route('/obtener_servidores', methods= ['GET'])
def obtener_servidore():
    """ Metodo para obtener los servidores con su nombre y descripcion."""
    try:
        servidores= ServidorController.obtener_servidores()
        return jsonify({'Servidores': servidores}), 200
    except:
        return jsonify({'mensaje':'No se encontro la pagina ...'}), 400
