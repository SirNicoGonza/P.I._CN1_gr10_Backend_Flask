from flask import Flask, jsonify
from api.datebase import DatabaseConnection

app = Flask(__name__)

@app.route('/prueba_db')
def prueba_db():
    # Realizar una consulta de ejemplo a la base de datos
    query = "SELECT * FROM usuarios"
    resultado = DatabaseConnection.fetch_all(query)
    
    return str(resultado)

if __name__ == '__main__':
    app.run()
