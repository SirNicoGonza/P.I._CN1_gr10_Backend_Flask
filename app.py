from flask import Flask, jsonify
from flask_cors import CORS
from api.datebase import DatabaseConnection

app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app, supports_credentials=True)



if __name__ == '__main__':
    app.run()
