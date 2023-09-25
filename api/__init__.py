from flask import Flask, jsonify, render_template, session
from flask_cors import CORS
from config import Config
from flask_session import Session
from .routes.rutas_bp import usuario_bp
from .datebase import DatabaseConnection
from flask_login import LoginManager
from .models.usuario_models import Usuario  
from flask_session import Session
import logging
logging.basicConfig(level=logging.DEBUG)  # Configura el nivel de registro DEBUG

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder=None, template_folder=None)
    app.config['SESSION_TYPE'] = 'filesystem'  
    Session(app)

    # Configurar CORS
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


    app.config.from_object(Config)

    DatabaseConnection.set_config(app.config)
    # Inicializar Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)  # Configurar Flask-Login

    # Registrar el blueprint para las rutas de usuario
    app.register_blueprint(usuario_bp, url_prefix='/usuario')

    # Configuramos la ruta para servir archivos estáticos desde el frontend
    frontend_folder = 'D:\\UPATECO\\proyecto_front\\frontend\\miappfrontend'
    app.static_folder = frontend_folder + '\\static'
    app.template_folder = frontend_folder + '\\templates'
    
    
    return app
   
   
    