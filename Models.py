from database import db
from flask_login import UserMixin
import bcrypt


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    fields = db.Relationship('Fields', backref='user')
    role = db.Column(db.String(100), nullable=False)

    def __init__(self,firstname, lastname, username, password, phone, role):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.phone = phone
        self.role = role


class Fields(db.Model):
    __tablename__ = 'fields'

    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey("users.id"))
    name = db.Column(db.String(100), nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Integer, nullable=False)



def initialiseDatabase():
    from main import app
    with app.app_context():
        db.drop_all()
        db.create_all()
        admin_User = Users(firstname='admin',
                           lastname='joe',
                           username='admin@email.com',
                           password='password123',
                           phone='07444400444',
                           role='admin')
        new_User = Users(firstname='Person',
                         lastname='Guy',
                         username='PersonGuy@email.xcom',
                         password='Green',
                         phone='07444477444',
                         role='users')
        db.session.add_all([admin_User,new_User])
        db.session.commit()

