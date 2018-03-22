from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "Hxx88F4snT"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:info3180project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
