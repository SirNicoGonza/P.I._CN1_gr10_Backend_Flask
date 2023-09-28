from flask import Blueprint, request, jsonify

from ..controller.mensaje_controller import MensajeController

#Se crea el Blueprint
mensaje_bp= Blueprint('mensaje',__name__)

@mensaje_bp.route('/modificar', methods= ['PUT'])
def modificar():
    """Metodo que para modificar un mensaje enviado. Recibe un json con el id_remitente y el contenido nuevo"""
    try:
        datos= request.json

        id_mensaje= datos.get('id_mensaje')
        mensaje_new= datos.get('mensaje_nuevo')

        modificado= MensajeController.modificar_mensaje(id_mensaje,mensaje_new)
        if modificado is not None:
            return jsonify({'mensaje':'se actualizo con exito'}), 200
        else:
            return jsonify({'error':'no se pudo modificar'}), 500
    except:
        return jsonify({'error':'no se encontro la pagina ...'}), 400



@mensaje_bp.route('/eliminar/<int:id_mensaje>', methods= ['DELETE'])
def eliminar_mensaje(id_mensaje):
    """ Metodo que elimina el mensaje que coicida con el id pasado por la ruta"""
    try:
        respuesta= MensajeController.eliminar_mensaje_id(id_mensaje)
        #print(respuesta)
        if respuesta['mensaje'] == 'mensaje eliminado':
            return jsonify({'Delete':'Se elimino con exito'}), 204
        elif respuesta['Error'] == 'no se pudo eliminar':
            return jsonify({'error': 'no se completo la operacio'}), 400
        else:
            return jsonify({'error': 'Formato de solicitud invalido'}), 400
            
    except:
        return jsonify({'error':'No se encontro la pagina ...'}), 400