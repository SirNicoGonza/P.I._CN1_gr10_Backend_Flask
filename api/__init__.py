from flask import Flask, jsonify
from flask_cors import CORS
from config import Config

from .routes.rutas_bp import usuario_bp
from .routes.rutas_servidor_bp import servidor_bp
from .routes.rutas_canal_bp import canal_bp
from .datebase import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(usuario_bp, url_prefix='/usuario')

    #Se registra el Blueprint de servidor
    app.register_blueprint(servidor_bp, url_prefix='/servidor')

    #Se registra el Blueprint de canales
    app.register_blueprint(canal_bp, url_prefix='/canal')
    
    return app
