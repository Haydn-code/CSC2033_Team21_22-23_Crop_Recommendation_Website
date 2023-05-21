from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

class signUpForm(FlaskForm):
    firstname = StringField()
    lastname = StringField()
    email = StringField()
    password = PasswordField()
    confirm_password = PasswordField()
    submit = SubmitField()

class loginForm(FlaskForm):
    email = StringField()
    password = PasswordField()
    submit = SubmitField()
