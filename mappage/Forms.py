from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class mapForm(FlaskForm):
    longitude = StringField('Longitude')
    latitude = StringField('Latitude')
    country_name = StringField('country_name')
    continent_name = StringField('continent_name')
    submit = SubmitField('Submit')
