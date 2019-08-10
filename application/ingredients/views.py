from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.ingredients.models import Ingredient
from application.ingredients.forms import IngredientForm, DeleteIngredientForm, UpdateIngredientForm


@app.route("/ingredients", methods=["GET"])
def ingredients_index():
    return render_template("ingredients/list.html", ingredients = Ingredient.query.order_by(Ingredient.id).all())

@app.route("/ingredients/new/")
@login_required
def ingredients_form():
    return render_template("ingredients/new.html", form = IngredientForm())

@app.route("/ingredients/update/")
@login_required
def ingredients_updateform():
    return render_template("ingredients/update.html", Ingredient.query.order_by(Ingredient.id).all(), form = UpdateIngredientForm())

@app.route("/ingredients/update/", methods=["POST"])
@login_required
def ingredients_update():

    form = UpdateIngredientForm(request.form)

    if not form.validate():
        return redirect(url_for("ingredients_updateform"))

#lisää tähän if-lause: jos id ylittää tietokannan maksimin, palauta virhe.
    ingredient_id = form.id.data
    ingredient = Ingredient.query.filter_by(id=ingredient_id).first()

    if form.name.data != "":
        ingredient.name = form.name.data

    db.session().commit()

    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/", methods=["POST"])
@login_required
def ingredients_create():

    form = IngredientForm(request.form)

    if not form.validate():
        return render_template("ingredients/new.html", form = form)

    g = Ingredient(form.name.data)

    db.session().add(g)
    db.session().commit()

    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/delete/", methods=["GET"])
@login_required
def ingredients_deleteform():

    return render_template("ingredients/delete.html", Ingredient.query.order_by(Ingredient.id).all(), form = DeleteIngredientForm())

@app.route("/ingredients/delete", methods=["POST"])
@login_required
def ingredients_delete():

    form = DeleteIngredientForm(request.form)

    if not form.validate():
        return render_template("ingredients/delete.html", form = form)

    del_id = form.id.data

    Ingredient.query.filter_by(id=del_id).delete()

    db.session.commit()

    return redirect(url_for("ingredients_index"))
