from flask import Flask, render_template
from app import app
from models import Medico, Agendamento

@app.route('/')
def index():
    m = Medico.query.get(1)
    return render_template('medico.html', medico=m)