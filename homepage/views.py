from flask import Blueprint, render_template

homepage_blueprint = Blueprint('Homepage', __name__, template_folder='Frontend')


@homepage_blueprint.route('/')
def homepage():
    return render_template('Homepage/index.html')
