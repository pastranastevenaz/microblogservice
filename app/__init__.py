from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.static_folder = 'static'
db = SQLAlchemy(app)

from app import views, models
