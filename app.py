from flask import Flask, render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from routes import setup_routes
from extensions import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "123456787"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///F:/Authentication-System-Flask/instance/database.db'

setup_routes(app)

db = SQLAlchemy(app)

app.static_folder = 'static'

if __name__ == '__main__':
    app.run(debug=True, port = 5001)