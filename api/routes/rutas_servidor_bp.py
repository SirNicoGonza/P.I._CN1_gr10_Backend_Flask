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

@servidor_bp.route('/obtener_servidor/<int:id_servidor>', methods= ['GET'])
def obtener_servidor_by_id(id_servidor):
    """Metodo que obtien el servidor que coincide con el id_servidor."""
    try:
        servidor= ServidorController.obtener_por_id(id_servidor)
        print(servidor)
        return jsonify({'servidor': servidor}), 200
    except:
        return jsonify({'error':'no se encontro la pagina'}), 400