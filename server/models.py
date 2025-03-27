from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
metadata = MetaData()

# Create an instance of SQLAlchemy
db = SQLAlchemy(metadata=metadata)

# Define the Earthquake model
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    # Define the columns of the Earthquake model
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"