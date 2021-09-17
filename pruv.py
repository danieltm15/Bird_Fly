from flask import Flask, request
app = Flask(__name__)

@app.route('/primeraruta')
def alguien_entro_a_la_ruta():
    return 'Mi primer backend!!!!'
