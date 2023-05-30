from flask import Blueprint, render_template, url_for

homepage_blueprint = Blueprint('Homepage', __name__, template_folder='Frontend')


@homepage_blueprint.route('/')
def homepage():
    about_image = url_for('static', filename='Projectimg/homepage_image_about2.jpg')
    donation_image = url_for('static', filename='Projectimg/home-donate.png')
    return render_template('Homepage/index.html', image1=about_image, image2=donation_image)
