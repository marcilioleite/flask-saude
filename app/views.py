from flask import Flask, render_template
from app import app
from models import Item

@app.route('/')
def index():
    item = Item.query.get(1)
    return render_template('item.html', title = item.nome)