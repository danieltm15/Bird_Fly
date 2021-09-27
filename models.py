from pruv import db

# Tabla aviones
class Aviones(db.Model): 
    __tablename__ = "Aviones"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String)
    añoFabricacion = db.Column(db.String)
    empresa = db.Column(db.String)

    def __init__(self, nombre, añoFabricacion, empresa):
        self.nombre = nombre
        self.añoFabricacion = añoFabricacion
        self.empresa = empresa
    
