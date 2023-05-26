import os
from flask import Flask
from dotenv import load_dotenv
from flask_login import LoginManager
from database import db

load_dotenv()

app = Flask(__name__, template_folder='Frontend')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO') == 'True'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.static_folder = 'static'

from users.Views import users_blueprint
from cropinfromationpage.views import cropinformation_blueprint
from homepage.views import homepage_blueprint
from donationpage.views import donation_blueprint
from mappage.views import mappage_blueprint

app.register_blueprint(cropinformation_blueprint)
app.register_blueprint(homepage_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(donation_blueprint)
app.register_blueprint(mappage_blueprint)

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.init_app(app)

from Models import Users


@login_manager.user_loader
def loadUser(id):
    return db.session.get(Users, int(id))

if __name__ == '__main__':
    app.run()
