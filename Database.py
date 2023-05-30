from flask_sqlalchemy import SQLAlchemy
# Creates the database in an external file to avoid cyclic import errors
db = SQLAlchemy()
