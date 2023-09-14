from flask import Flask, jsonify
from flask_cors import CORS
from config import Config

from .routes.rutas_bp import usuario_bp
from .datebase import DatabaseConnection
#from .models.exceptions import CustomException, FilmNotFound,InvalidDataError  # Importamos las excepciones necesarias

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(usuario_bp, url_prefix='/user')

    return app

