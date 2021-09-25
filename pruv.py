from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db=SQLAlchemy(app)

@app.route('/ruta')
def alguien_entro_a_la_ruta():
    return 'Hola daniel'

@app.route('/destinos')
def volar():
    return 'Estos son los destinos del avion'

@app.route('/')
def ruta_raiz():
    return 'Bienvenido a bird fly!'

# Rutas de accion

@app.route('/bird', methods=["GET","POST"])
def crud_Bird():
    if request.method=="GET":
        print("Se solicito un avion")
        return "Nos soliccitan un avion"
    elif request.method=="POST":
        request_data = request.form
        company = request_data["company"]
        destination = request_data["destination"]
        time = request_data["time"]
        print("Se envia un avion")
        return "Solicitaron un avion de " + company  + " para " + destination + " para las " + time
