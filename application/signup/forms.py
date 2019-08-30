from flask_wtf import FlaskForm
from wtforms import StringField, validators
from application.auth.models import User

class SignUpForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1)])
    username = StringField("Username", [validators.Length(min=1)])
    password = StringField("Password", [validators.Length(min=1)])

    class Meta:
        csrf = False
