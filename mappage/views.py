from flask import Blueprint, render_template

mappage_blueprint = Blueprint('Mappage', __name__, template_folder='Frontend')


@mappage_blueprint.route('/mappage')
def homepage():
    return render_template('Mappage/map.html')
