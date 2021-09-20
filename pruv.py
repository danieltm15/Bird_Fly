from flask import Flask, request
app = Flask(__name__)

@app.route('/ruta')
def alguien_entro_a_la_ruta():
    return 'Hola daniel'
