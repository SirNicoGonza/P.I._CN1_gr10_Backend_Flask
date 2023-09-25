from flask import Blueprint, request, jsonify

from ..controller.canal_controller import CanalController

#Se crea el Blueprint
canal_bp= Blueprint('canal',__name__)

#Rutas
@canal_bp.route('/modificar_nombre/<int:id_canal>', methods=['PUT'])
def modificar_nombrel(id_canal):
    """Metodo que serive para modificar el nombre del canal"""
    try:
        registro= request.json
        datos= registro.get('nombre'), id_canal
        CanalController.actualizar_nombre(datos)
        return jsonify({'servidor':'Servidor actualizado'}),200
    except:
        return jsonify({'error':'No se encontro la pagina ...'}), 400