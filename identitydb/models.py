from identitydb import db
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    dob = db.Column(db.String(80))
    address = db.Column(db.String(80))  
    passport = db.Column(db.String(80))

    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.address}')"
