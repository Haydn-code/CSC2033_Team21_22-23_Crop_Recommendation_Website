from flask import Blueprint, render_template

donation_blueprint = Blueprint('Donationpage', __name__, template_folder='Frontend')


@donation_blueprint.route('/donationspage')
def homepage():
    return render_template('Donationpage/donations.html')
