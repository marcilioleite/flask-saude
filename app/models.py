from app import db

class Item(db.Model):
    __tablename__ = 'itens'
    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column(db.String(45))