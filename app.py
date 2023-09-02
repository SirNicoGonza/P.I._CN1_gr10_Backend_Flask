from controllers import app

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/practida')
def practica():
    return {'mensaje':'Es una practica'}