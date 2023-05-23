from main import db, app


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    fields = db.Relationship('Field', backref='user')
    role = db.Column(db.String(100), nullable=False)

    def __init__(self,firstname, lastname, username, password, phone, role):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.phone = phone
        self.role = role


class Fields(db.Model):
    __tablename__ = 'fields'

    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey("users.id"))
    longitude = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Integer, nullable=False)

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude


def initialiseDatabase():
    with app.app_context():
        db.drop_all()
        db.create_all()
        admin_User = Users(firstname='admin',
                           lastname='joe',
                           username='admin@email.com',
                           password='password123',
                           phone='07444400444',
                           role='admin')
        db.session.add(admin_User)
        db.session.commit()

