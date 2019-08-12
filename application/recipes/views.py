from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db

from application.recipes.models import Recipe, RecipeIngredient
from application.recipes.forms import RecipeForm, DeleteForm, UpdateForm

from application.ingredients.models import Ingredient

from application.auth.models import User

@app.route("/recipes/", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.order_by(Recipe.id).all())

@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/update/")
@login_required
def recipes_updateform():
    return render_template("recipes/update.html", form = UpdateForm(), recipes = Recipe.query.order_by(Recipe.id).all())

@app.route("/recipes/update/", methods=["POST"])
@login_required
def recipes_update():

    form = UpdateForm(request.form)

    if not form.validate():
        return redirect(url_for("recipes_updateform"))

#lisää tähän if-lause: jos id ylittää tietokannan maksimin, palauta virhe.
    recipe_id = form.id.data
    recipe = Recipe.query.filter_by(id=recipe_id).first()

    if form.name.data != "":
        recipe.name = form.name.data

    if form.timeNeeded.data is not None:
        recipe.timeNeeded = form.timeNeeded.data

    if form.instructions.data != "":
        recipe.instructions = form.instructions.data

    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/", methods=["POST"])
@login_required
def recipes_create():

# Muuta RecipeForm ja muut ja lisää sinne oma kohta RecipeIngredientin luomiselle. Esim. 10 RecipeIngredientiä kerralla niin homma toimii. Etsi reseptiä nimen perusteella.

    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)

    r = Recipe(form.name.data, form.timeNeeded.data, form.instructions.data)
    r.account_id = current_user.id

    db.session().add(r)
    db.session().flush()

    if form.ingredient_name1.data and form.quantity1.data:
        ing = Ingredient.query.filter_by(name=form.ingredient_name1.data).first()
        recipeing = RecipeIngredient(form.quantity1.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.id
        db.session().add(recipeing)

    if form.ingredient_name2.data and form.quantity2.data:
        ing = Ingredient.query.filter_by(name=form.ingredient_name2.data).first()
        recipeing = RecipeIngredient(form.quantity2.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.id
        db.session().add(recipeing)

    if form.ingredient_name3.data and form.quantity3.data:
        ing = Ingredient.query.filter_by(name=form.ingredient_name3.data).first()
        recipeing = RecipeIngredient(form.quantity3.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.id
        db.session().add(recipeing)

    if form.ingredient_name4.data and form.quantity4.data:
        ing = Ingredient.query.filter_by(name=form.ingredient_name4.data).first()
        recipeing = RecipeIngredient(form.quantity4.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.id
        db.session().add(recipeing)

    if form.ingredient_name5.data and form.quantity5.data:
        ing = Ingredient.query.filter_by(name=form.ingredient_name5.data).first()
        recipeing = RecipeIngredient(form.quantity5.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.id
        db.session().add(recipeing)

    if form.ingredient_name6.data and form.quantity6.data:
        ing = Ingredient.query.filter_by(name=form.ingredient_name6.data).first()
        recipeing = RecipeIngredient(form.quantity6.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.id
        db.session().add(recipeing)

    if form.ingredient_name7.data and form.quantity7.data:
        ing = Ingredient.query.filter_by(name=form.ingredient_name7.data).first()
        recipeing = RecipeIngredient(form.quantity7.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.id
        db.session().add(recipeing)

    if form.ingredient_name8.data and form.quantity8.data:
        ing = Ingredient.query.filter_by(name=form.ingredient_name8.data).first()
        recipeing = RecipeIngredient(form.quantity8.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.id
        db.session().add(recipeing)

    if form.ingredient_name9.data and form.quantity9.data:
        ing = Ingredient.query.filter_by(name=form.ingredient_name9.data).first()
        recipeing = RecipeIngredient(form.quantity9.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.id
        db.session().add(recipeing)

    if form.ingredient_name10.data and form.quantity10.data:
        ing = Ingredient.query.filter_by(name=form.ingredient_name10.data).first()
        recipeing = RecipeIngredient(form.quantity10.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.id
        db.session().add(recipeing)

    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/topcontributors/", methods=["GET"])
@login_required
def recipes_topcontributors():

    return render_template("recipes/topcontributors.html", topcontributors=User.list_top_contributors())

@app.route("/recipes/delete/", methods=["GET"])
@login_required
def recipes_deleteform():

    return render_template("recipes/delete.html", form = DeleteForm(), recipes = Recipe.query.order_by(Recipe.id).all())

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
