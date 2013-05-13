from flask import url_for, redirect, render_template, flash, g, session
from app import app
from models import Agendamento

@app.route('/')
def index():
    return "Hello, World!"