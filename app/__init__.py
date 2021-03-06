from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/saude'
app.config['BOOTSTRAP_FONTAWESOME'] = True
db = SQLAlchemy(app)

from app import models, views