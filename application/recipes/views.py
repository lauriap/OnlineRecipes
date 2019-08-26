from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required

from application.recipes.models import Recipe, RecipeIngredient
from application.recipes.forms import RecipeForm, DeleteForm, UpdateForm

from application.ingredients.models import Ingredient

from application.auth.models import User

@app.route("/")
def start_page():
    return render_template("/index.html")


@app.route("/recipes/", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.order_by(Recipe.id).all())


@app.route("/recipes/<recipe_id>/", methods=["GET"])
def show_recipe(recipe_id):

    query_ingredients = Ingredient.query.join(RecipeIngredient).join(Recipe).filter((RecipeIngredient.recipe_id == recipe_id) and (RecipeIngredient.ingredient_id == Ingredient.id)).all()

    return render_template("recipes/fullrecipe.html", recipe=Recipe.query.filter_by(id=recipe_id).first(), recipe_ingredients=RecipeIngredient.query.filter_by(recipe_id=recipe_id).all(), ingredients=query_ingredients)


@app.route("/recipes/new/")
@login_required(role="ADMIN")
def recipes_form():

    return render_template("recipes/new.html", form = RecipeForm())


@app.route("/recipes/update/<recipe_id>", methods=["GET"])
@login_required(role="ADMIN")
def recipes_updateform(recipe_id):

    recipe=Recipe.query.filter_by(id=recipe_id).first()
    recipe_ingredients=RecipeIngredient.query.filter_by(recipe_id=recipe_id).all()
    query_ingredients = Ingredient.query.join(RecipeIngredient).join(Recipe).filter((RecipeIngredient.recipe_id == recipe_id) and (RecipeIngredient.ingredient_id == Ingredient.id)).all()

    updateform = UpdateForm()

    updateform.id.data = recipe.id
    updateform.name.data = recipe.name
    updateform.timeNeeded.data = recipe.timeNeeded
    updateform.instructions.data = recipe.instructions

    updateform.ingredient_1.data = query_ingredients[0]
    updateform.quantity_1.data = recipe_ingredients[0].amount

    try:
        updateform.ingredient_2.data = query_ingredients[1]
        updateform.quantity_2.data = recipe_ingredients[1].amount
    except:
        pass

    try:
        updateform.ingredient_3.data = query_ingredients[2]
        updateform.quantity_3.data = recipe_ingredients[2].amount
    except:
        pass

    try:
        updateform.ingredient_4.data = query_ingredients[3]
        updateform.quantity_4.data = recipe_ingredients[3].amount
    except:
        pass

    try:
        updateform.ingredient_5.data = query_ingredients[4]
        updateform.quantity_5.data = recipe_ingredients[4].amount
    except:
        pass

    try:
        updateform.ingredient_6.data = query_ingredients[5]
        updateform.quantity_6.data = recipe_ingredients[5].amount
    except:
        pass

    try:
        updateform.ingredient_7.data = query_ingredients[6]
        updateform.quantity_7.data = recipe_ingredients[6].amount
    except:
        pass

    try:
        updateform.ingredient_8.data = query_ingredients[7]
        updateform.quantity_8.data = recipe_ingredients[7].amount
    except:
        pass

    try:
        updateform.ingredient_9.data = query_ingredients[8]
        updateform.quantity_9.data = recipe_ingredients[8].amount
    except:
        pass

    try:
        updateform.ingredient_10.data = query_ingredients[9]
        updateform.quantity_10.data = recipe_ingredients[9].amount
    except:
        pass



    return render_template("recipes/update.html", form = updateform, recipe=Recipe.query.filter_by(id=recipe_id).first(), recipe_ingredients=RecipeIngredient.query.filter_by(recipe_id=recipe_id).all(), ingredients=query_ingredients)


@app.route("/recipes/update/", methods=["POST"])
@login_required(role="ADMIN")
def recipes_update():

    form = UpdateForm(request.form)

    if not form.validate():
        return render_template("recipes/update.html", form = form)

    r = Recipe(form.name.data, form.timeNeeded.data, form.instructions.data)
    r.account_id = current_user.id
    r.id = form.id.data

    # call database objects
    recipe=Recipe.query.filter_by(id=form.id.data).first()
    recipe_ingredients=RecipeIngredient.query.filter_by(recipe_id=recipe.id).all()
    query_ingredients = Ingredient.query.join(RecipeIngredient).join(Recipe).filter((RecipeIngredient.recipe_id == recipe.id) and (RecipeIngredient.ingredient_id == Ingredient.id)).all()

    # update recipe information
    recipe.id = form.id.data
    recipe.name = form.name.data
    recipe.timeNeeded = form.timeNeeded.data
    recipe.instructions = form.instructions.data

    if form.ingredient_1.data and form.quantity_1.data:
        # update ingredient_id and amount for recipe_ingredient
        try:
            recipe_ingredients[0].ingredient_id = form.ingredient_1.data.get_id()
            recipe_ingredients[0].amount = form.quantity_1.data
        except:
            # if the user is adding new ingredients and quantities, this takes care of it
            ing=form.ingredient_1.data
            recipeing = RecipeIngredient(form.quantity_1.data)

            recipeing.recipe_id = recipe.id
            recipeing.ingredient_id = ing.get_id()
            db.session().add(recipeing)


    if form.ingredient_2.data and form.quantity_2.data:
        # update ingredient_id and amount for recipe_ingredient
        try:
            recipe_ingredients[1].ingredient_id = form.ingredient_2.data.get_id()
            recipe_ingredients[1].amount = form.quantity_2.data
        except:
            #EI TOIMI AINAKAAN TÄLLAISENAAN!!!
            if not form.ingredient_2.data and len(recipe_ingredients) >= 2:
                    RecipeIngredient.query.filter_by(id=recipe_ingredients[1].id).delete()
            else:
            # if the user is adding new ingredients and quantities, this takes care of it
                ing=form.ingredient_2.data
                recipeing = RecipeIngredient(form.quantity_2.data)

                recipeing.recipe_id = recipe.id
                recipeing.ingredient_id = ing.get_id()
                db.session().add(recipeing)

    if form.ingredient_3.data and form.quantity_3.data:
        # update ingredient_id and amount for recipe_ingredient
        try:
            recipe_ingredients[2].ingredient_id = form.ingredient_3.data.get_id()
            recipe_ingredients[2].amount = form.quantity_3.data
        except:
            # if the user is adding new ingredients and quantities, this takes care of it
            ing=form.ingredient_3.data
            recipeing = RecipeIngredient(form.quantity_3.data)

            recipeing.recipe_id = recipe.id
            recipeing.ingredient_id = ing.get_id()
            db.session().add(recipeing)

    if form.ingredient_4.data and form.quantity_4.data:
        # update ingredient_id and amount for recipe_ingredient
        try:
            recipe_ingredients[3].ingredient_id = form.ingredient_4.data.get_id()
            recipe_ingredients[3].amount = form.quantity_4.data
        except:
            # if the user is adding new ingredients and quantities, this takes care of it
            ing=form.ingredient_4.data
            recipeing = RecipeIngredient(form.quantity_4.data)

            recipeing.recipe_id = recipe.id
            recipeing.ingredient_id = ing.get_id()
            db.session().add(recipeing)

    if form.ingredient_5.data and form.quantity_5.data:
        # update ingredient_id and amount for recipe_ingredient
        try:
            recipe_ingredients[4].ingredient_id = form.ingredient_5.data.get_id()
            recipe_ingredients[4].amount = form.quantity_5.data
        except:
            # if the user is adding new ingredients and quantities, this takes care of it
            ing=form.ingredient_5.data
            recipeing = RecipeIngredient(form.quantity_5.data)

            recipeing.recipe_id = recipe.id
            recipeing.ingredient_id = ing.get_id()
            db.session().add(recipeing)

    if form.ingredient_6.data and form.quantity_6.data:
        # update ingredient_id and amount for recipe_ingredient
        try:
            recipe_ingredients[5].ingredient_id = form.ingredient_6.data.get_id()
            recipe_ingredients[5].amount = form.quantity_6.data
        except:
            # if the user is adding new ingredients and quantities, this takes care of it
            ing=form.ingredient_6.data
            recipeing = RecipeIngredient(form.quantity_6.data)

            recipeing.recipe_id = recipe.id
            recipeing.ingredient_id = ing.get_id()
            db.session().add(recipeing)

    if form.ingredient_7.data and form.quantity_7.data:
        # update ingredient_id and amount for recipe_ingredient
        try:
            recipe_ingredients[6].ingredient_id = form.ingredient_7.data.get_id()
            recipe_ingredients[6].amount = form.quantity_7.data
        except:
            # if the user is adding new ingredients and quantities, this takes care of it
            ing=form.ingredient_7.data
            recipeing = RecipeIngredient(form.quantity_7.data)

            recipeing.recipe_id = recipe.id
            recipeing.ingredient_id = ing.get_id()
            db.session().add(recipeing)

    if form.ingredient_8.data and form.quantity_8.data:
        # update ingredient_id and amount for recipe_ingredient
        try:
            recipe_ingredients[7].ingredient_id = form.ingredient_8.data.get_id()
            recipe_ingredients[7].amount = form.quantity_8.data
        except:
            # if the user is adding new ingredients and quantities, this takes care of it
            ing=form.ingredient_8.data
            recipeing = RecipeIngredient(form.quantity_8.data)

            recipeing.recipe_id = recipe.id
            recipeing.ingredient_id = ing.get_id()
            db.session().add(recipeing)

    if form.ingredient_9.data and form.quantity_9.data:
        # update ingredient_id and amount for recipe_ingredient
        try:
            recipe_ingredients[8].ingredient_id = form.ingredient_9.data.get_id()
            recipe_ingredients[8].amount = form.quantity_9.data
        except:
            # if the user is adding new ingredients and quantities, this takes care of it
            ing=form.ingredient_9.data
            recipeing = RecipeIngredient(form.quantity_9.data)

            recipeing.recipe_id = recipe.id
            recipeing.ingredient_id = ing.get_id()
            db.session().add(recipeing)

    if form.ingredient_10.data and form.quantity_10.data:
        # update ingredient_id and amount for recipe_ingredient
        try:
            recipe_ingredients[9].ingredient_id = form.ingredient_10.data.get_id()
            recipe_ingredients[9].amount = form.quantity_10.data
        except:
            # if the user is adding new ingredients and quantities, this takes care of it
            ing=form.ingredient_10.data
            recipeing = RecipeIngredient(form.quantity_10.data)

            recipeing.recipe_id = recipe.id
            recipeing.ingredient_id = ing.get_id()
            db.session().add(recipeing)

    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/", methods=["POST"])
@login_required(role="ADMIN")
def recipes_create():

    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form = form)

    r = Recipe(form.name.data, form.timeNeeded.data, form.instructions.data)
    r.account_id = current_user.id

    db.session().add(r)
    db.session().flush()

    if form.ingredient_1.data and form.quantity_1.data:
        ing=form.ingredient_1.data
        recipeing = RecipeIngredient(form.quantity_1.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.get_id()
        db.session().add(recipeing)

    if form.ingredient_2.data and form.quantity_2.data:
        ing=form.ingredient_2.data
        recipeing = RecipeIngredient(form.quantity_2.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.get_id()
        db.session().add(recipeing)

    if form.ingredient_3.data and form.quantity_3.data:
        ing=form.ingredient_3.data
        recipeing = RecipeIngredient(form.quantity_3.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.get_id()
        db.session().add(recipeing)

    if form.ingredient_4.data and form.quantity_4.data:
        ing=form.ingredient_4.data
        recipeing = RecipeIngredient(form.quantity_4.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.get_id()
        db.session().add(recipeing)

    if form.ingredient_5.data and form.quantity_5.data:
        ing=form.ingredient_5.data
        recipeing = RecipeIngredient(form.quantity_5.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.get_id()
        db.session().add(recipeing)

    if form.ingredient_6.data and form.quantity_6.data:
        ing=form.ingredient_6.data
        recipeing = RecipeIngredient(form.quantity_6.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.get_id()
        db.session().add(recipeing)

    if form.ingredient_7.data and form.quantity_7.data:
        ing=form.ingredient_7.data
        recipeing = RecipeIngredient(form.quantity_7.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.get_id()
        db.session().add(recipeing)

    if form.ingredient_8.data and form.quantity_8.data:
        ing=form.ingredient_8.data
        recipeing = RecipeIngredient(form.quantity_8.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.get_id()
        db.session().add(recipeing)

    if form.ingredient_9.data and form.quantity_9.data:
        ing=form.ingredient_9.data
        recipeing = RecipeIngredient(form.quantity_9.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.get_id()
        db.session().add(recipeing)

    if form.ingredient_10.data and form.quantity_10.data:
        ing=form.ingredient_10.data
        recipeing = RecipeIngredient(form.quantity_10.data)

        recipeing.recipe_id = r.id
        recipeing.ingredient_id = ing.get_id()
        db.session().add(recipeing)

    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/topcontributors/", methods=["GET"])
@login_required(role="ADMIN")
def recipes_topcontributors():

    return render_template("recipes/topcontributors.html", topcontributors=User.list_top_contributors())


@app.route("/recipes/delete/", methods=["GET"])
@login_required(role="ADMIN")
def recipes_deleteform():

    return render_template("recipes/delete.html", form = DeleteForm(), recipes = Recipe.query.order_by(Recipe.id).all())

@app.route("/recipes/delete", methods=["POST"])
@login_required(role="ADMIN")
def recipes_delete():

    form = DeleteForm(request.form)

    if not form.validate():
        return render_template("recipes/delete.html", form = form)

    del_recipe = form.id.data

    RecipeIngredient.query.filter_by(recipe_id=del_recipe.get_id()).delete()
    Recipe.query.filter_by(id=del_recipe.get_id()).delete()

    db.session.commit()

    return redirect(url_for("recipes_index"))
