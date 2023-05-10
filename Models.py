from main import db, app


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    fields = db.Relationship('Field', backref='user')

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Fields(db.Model):
    __tablename__ = 'fields'

    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey("users.id"))
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)

    def __init__(self, x, y):
        self.x = x
        self.y = y


def initialiseDatabase():
    with app.app_context():
        db.drop_all()
        db.create_all()

