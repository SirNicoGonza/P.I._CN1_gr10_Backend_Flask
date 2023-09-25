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

@canal_bp.route('/eliminar_canal/<int:id_canal>', methods= ['DELETE'])
def eliminar_canal(id_canal):
    """ Metodo que elimina el servidor pasado por id."""
    try:
        respuesta=CanalController.eliminar_canal_id(id_canal)
        #print(respuesta)
        if respuesta['mensaje'] == 'canal eliminado':
            return jsonify({'Delete':'Se elimino con exito'}), 204
        elif respuesta['Error'] == 'no se pudo eliminar':
            return jsonify({'error': 'no se completo la operacio'}), 400
        else:
            return jsonify({'error': 'Formato de solicitud invalido'}), 400
            
    except:
        return jsonify({'error':'No se encontro la pagina ...'}), 400