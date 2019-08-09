from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=1)])
    timeNeeded = IntegerField("Time needed", [validators.NumberRange(min=1)])
    instructions = TextAreaField("Instructions", [validators.Length(min=1)])

    class Meta:
        csrf = False


class DeleteForm(FlaskForm):
    id = IntegerField("Recipe number", [validators.NumberRange(min=1, message="Please select a recipe number from the list below.")])

    class Meta:
        csrf = False

class UpdateForm(FlaskForm):
    id = IntegerField("Recipe number", [validators.NumberRange(min=1, message="Please select a recipe number from the list below.")])
    name = StringField("New recipe name", [validators.Optional()])
    timeNeeded = IntegerField("New time", [validators.Optional()])
    instructions = StringField("New instructions", [validators.Optional()])

    class Meta:
        csrf = False

