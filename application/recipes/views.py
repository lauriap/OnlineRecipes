from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm, DeleteForm


@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/update/")
@login_required
def recipes_updateform():
    return render_template("recipes/update.html", recipes = Recipe.query.all())

@app.route("/recipes/update/", methods=["POST"])
@login_required
def recipes_update():

    recipe_id = request.form.get("id")
    recipe = Recipe.query.filter_by(id=recipe_id).first()

    newName = request.form.get("name")
    newTimeNeeded = request.form.get("timeNeeded")
    newInstructions = request.form.get("instructions")

    if newName != "":
        recipe.name = newName

    if newTimeNeeded != "":
        recipe.timeNeeded = newTimeNeeded

    if newInstructions != "":
        recipe.instructions = newInstructions

    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/", methods=["POST"])
@login_required
def recipes_create():

    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)

    r = Recipe(form.name.data, form.timeNeeded.data, form.instructions.data)
    r.account_id = current_user.id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/delete/", methods=["GET"])
@login_required
def recipes_deleteform():

    return render_template("recipes/delete.html", form = DeleteForm(), recipes = Recipe.query.all())

@app.route("/recipes/delete", methods=["POST"])
@login_required
def recipes_delete():

    form = DeleteForm(request.form)

    if not form.validate():
        return render_template("recipes/delete.html", form = form)

    del_id = form.id.data

    Recipe.query.filter_by(id=del_id).delete()

    db.session.commit()

    return redirect(url_for("recipes_index"))
