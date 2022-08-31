from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from identitydb import db
from identitydb.models import User
import os
from PIL import Image
from flask import current_app

identity = Blueprint('identity', __name__)

@identity.route("/")
def home():
    return """
    <h1> ONLINE DB </h1>
    <a href='/register'>Register</a>
    """

@identity.route("/data")
def congrats():
    user = User.query.all()
    return render_template("data.html", users=user)

@identity.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        dob = request.form["dob"]
        address = request.form["address"]
        passport = request.form["passport"]
        print(fname)
        print(lname)
        print(dob)
        print(address,"<- error code")
        print(passport)
        user = User(firstname=fname, lastname=lname, address=address, dob=dob, passport=passport)
        db.session.add(user)
        db.session.commit()
        return redirect(congrats)
    else:
        return render_template("register.html")
