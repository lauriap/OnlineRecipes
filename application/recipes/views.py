from application import app, db
from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipe

@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/new/")
def recipes_form():
    return render_template("recipes/new.html")

@app.route("/recipes/", methods=["POST"])
def recipes_create():
    r = Recipe(request.form.get("name"), request.form.get("timeNeeded"), request.form.get("instructions"))

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("recipes_index"))