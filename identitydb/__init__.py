from flask import Flask, redirect, render_template, request, flash, abort, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
import json

app = Flask(__name__)
# app.config['SECRET_KEY'] = "y8uiyuviubuyw3-3wtswcvywcu"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)


def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = "y8uiyuviubuyw3-3wtswcvywcu"
	app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
	db = SQLAlchemy(app)

	from identitydb.routes import identity
	app.register_blueprint(identity)

	return app
