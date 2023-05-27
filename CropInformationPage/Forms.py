from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class searchCropForm(FlaskForm):
    search = StringField(validators=[DataRequired(), Length(max=50)])
    submit = SubmitField()