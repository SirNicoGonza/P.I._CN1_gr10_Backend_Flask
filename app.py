from controllers import app

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/practida')
def practica():
    """ Es este es un endpoint para practicar"""
    return {'mensaje':'Es una practica'}