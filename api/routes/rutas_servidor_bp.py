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
        return jsonify({'servidor': servidor}), 200
    except:
        return jsonify({'error':'no se encontro la pagina'}), 400

@servidor_bp.route('/obtener_servidor/<string:nombre_servidor>', methods= ['GET'])
def obtener_servidor_by_nombre(nombre_servidor):
    """Metodo que obtien el servidor que coincide con el id_servidor."""
    try:
        servidor= ServidorController.obtener_por_nombre(nombre_servidor)
        return jsonify({'servidor': servidor}), 200
    except:
        return jsonify({'error':'no se encontro la pagina'}), 400

@servidor_bp.route('/actualizar_nombre/<int:id_servidor>', methods=['PUT'])
def actualizar_nombre_servidor(id_servidor):
    try:
        registro= request.json
        datos= registro.get('nombre'), id_servidor
        ServidorController.actualizar_nombre(datos)
        return jsonify({'servidor':'Servidor actualizado'}),200
    except:
        return jsonify({'error':'No se encontro la pagina ...'}), 400

@servidor_bp.route('/canales_del_servidor/<int:id_servidor>', methods=['GET'])
def obtener_canales(id_servidor):
    """ Metodo que obtiene todos los canales de un servidor que coicida con el id."""
    try:
        canales= ServidorController.obtener_todos_canales(id_servidor)
        if canales is not None:
            return jsonify({'servidor': id_servidor, 'canales': canales}), 200
        else:
            return jsonify({'mensaje': 'El servidor no tiene canales'}), 200
    except:
        return jsonify({'error': 'no se encontro la pagina ...'}), 400

@servidor_bp.route('/eliminar_servidor/<int:id_servidor>', methods= ['DELETE'])
def eliminar_servidor(id_servidor):
    """ Metodo que elimina el servidor pasado por id."""
    try:
        respuesta=ServidorController.eliminar_servidor_id(id_servidor)
        #print(respuesta)
        if respuesta['mensaje'] == 'servidor eliminado':
            return jsonify({'Delete':'Se elimino con exito'}), 204
        elif respuesta['Error'] == 'no se pudo eliminar':
            return jsonify({'error': 'no se completo la operacio'}), 400
        else:
            return jsonify({'error': 'Formato de solicitud invalido'}), 400
            
    except:
        return jsonify({'error':'No se encontro la pagina ...'}), 400