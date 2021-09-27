
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/birdbd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'


db=SQLAlchemy(app)

from models import Aviones

db.create_all()
db.session.commit()



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

        nombre = "icaro"
        fecha= "12-23-21"
        empresa="avianca"

        avion = Aviones(nombre, fecha, empresa)

        db.session.add(avion)
        db.session.commit()

        print("Se solicito un avion")
        return "Nos soliccitan un avion"
    elif request.method=="POST":
        request_data = request.form
        company = request_data["company"]
        destination = request_data["destination"]
        time = request_data["time"]
        print("Se envia un avion")
        return "Solicitaron un avion de " + company  + " para " + destination + " para las " + time
