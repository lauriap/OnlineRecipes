from application import app, db
from application.auth.models import User

from flask import redirect, render_template, request, url_for

@app.route("/signup/")
def signup_form():
    return render_template("/signup/signup.html")

@app.route("/signup/", methods=["POST"])
def signup_create():
    s = User(request.form.get("name"), request.form.get("username"), request.form.get("password"))

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("auth_login"))
