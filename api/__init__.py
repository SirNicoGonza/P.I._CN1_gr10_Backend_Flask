from flask import Flask, jsonify, render_template
from flask_cors import CORS
from config import Config

from .routes.rutas_bp import usuario_bp
from .datebase import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder=None, template_folder=None)

    # Configurar CORS
    CORS(app, supports_credentials=True)

    app.config.from_object(Config)

    DatabaseConnection.set_config(app.config)

    # Registrar el blueprint para las rutas de usuario
    app.register_blueprint(usuario_bp, url_prefix='/usuario')

    # Configuramos la ruta para servir archivos estáticos desde el frontend
    frontend_folder = 'D:\\UPATECO\\proyecto_front\\frontend\\miappfrontend'
    app.static_folder = frontend_folder + '\\static'
    app.template_folder = frontend_folder + '\\templates'

    @app.route('/', methods=['GET'])
    def index():
        
        return render_template('index.html')
    
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404
    return app
