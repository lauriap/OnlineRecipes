from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=1)])
    timeNeeded = IntegerField("Time needed")
    instructions = TextAreaField("Instructions", [validators.Length(min=1)]) 

    class Meta:
        csrf = False


class DeleteForm(FlaskForm):
    id = IntegerField("Recipe number")

    class Meta:
        csrf = False

