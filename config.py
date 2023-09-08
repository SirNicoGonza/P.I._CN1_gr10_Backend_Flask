from dotenv import dotenv_values
class Config:
    config = dotenv_values(".env")
 
    SECRET_KEY = config['SECRET_KEY']
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    DATABASE_USERNAME = config['DATABASE_USERNAME']
    DATABASE_PASSWORD = config['DATABASE_PASSWORD']
    DATABASE_HOST = config['DATABASE_HOST']
    DATABASE_PORT = config['DATABASE_PORT']
    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"