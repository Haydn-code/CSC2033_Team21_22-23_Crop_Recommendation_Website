from flask import Blueprint, render_template

cropinformation_blueprint = Blueprint('Cropinformationpage', __name__, template_folder='Frontend')


@cropinformation_blueprint.route('/cropinformationpage')
def cropinfromationpage():
    return render_template('Cropinformationpage/crop-information.html')