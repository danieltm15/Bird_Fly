from pruv import db

# Tabla aviones
class Aviones(db.Model): 
    __tablename__ = "Aviones"
    id = db.Column(db.Integer, primary_Key=True)
    nombre = db.Column(db.String)
    añoFabricacion = db.Column(db.String)
    empresa = db.Column(db.String)
    
