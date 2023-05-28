from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class signUpForm(FlaskForm):
    first_name = StringField(validators=[DataRequired(), Length(max=50)])
    last_name = StringField(validators=[DataRequired(), Length(max=50)])
    phone = StringField(validators=[DataRequired(), Length(min=11, max=11, message="Must be 11 numbers long")])
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired(), EqualTo(fieldname='confirm_password',
                                                                 message='Passwords must match')])
    confirm_password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()

class loginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()

class searchFarmForm(FlaskForm):
    longitude = FloatField(validators=[DataRequired()])
    latitude = FloatField(validators=[DataRequired()])
    farm_name = StringField(validators=[DataRequired()])
    submit = SubmitField()
