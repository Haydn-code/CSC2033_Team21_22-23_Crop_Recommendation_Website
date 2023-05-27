from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class mapForm(FlaskForm):
    longitude = StringField('Longitude')
    latitude = StringField('Latitude')
    submit = SubmitField('Submit')
