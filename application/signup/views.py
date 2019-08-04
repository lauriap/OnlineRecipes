from application import app, db
from application.auth.models import User
from application.signup.forms import SignUpForm

from flask import redirect, render_template, request, url_for

@app.route("/signup/")
def signup_form():
    return render_template("/signup/signup.html", form = SignUpForm())

@app.route("/signup/", methods=["POST"])
def signup_create():
    form = SignUpForm(request.form)

    if not form.validate():
        return render_template("signup/signup.html", form = form)

    s = User(form.name.data, form.username.data, form.password.data)

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("auth_login"))
