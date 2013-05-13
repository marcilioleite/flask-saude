from app import db

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    