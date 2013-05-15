from flask import Flask, render_template
from app import app
from models import Paciente, Consulta

@app.route('/')
def index():
    return "Hello, world"