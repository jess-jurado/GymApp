from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ejercicio(db.Model):
    __tablename__ = 'Ejercicios'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_ejercicio = db.Column(db.String(255), nullable=False)
    grupo_muscular = db.Column(db.String(100))
    subgrupo_muscular = db.Column(db.String(100))
    imagen_url = db.Column(db.String(500))

class Rutina(db.Model):
    __tablename__ = 'Rutinas'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), nullable=False)
    nombre_rutina = db.Column(db.String(255), nullable=False)
    id_ejercicio = db.Column(db.Integer, db.ForeignKey('Ejercicios.id'), nullable=False)
    dia = db.Column(db.String(50))
