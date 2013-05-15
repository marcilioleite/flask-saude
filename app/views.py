from flask import Flask, render_template
from app import app
from models import Medico, Agendamento

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    m = Medico.query.get(1)
    return render_template('medico.html', medico=m)