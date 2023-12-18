from flask_sqlalchemy import SQLAlchemy

# Create an instance of the SQLAlchemy class
db = SQLAlchemy()

# Define a Pet class that represents a pet available for adoption
class Pet(db.Model):
    """
    Represents a pet available for adoption.
    """

    # Define the table name for the Pet class
    __tablename__ = "pets"

    # Define the columns for the Pet table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Unique identifier for the pet
    name = db.Column(db.String(50), nullable=False)  # Name of the pet
    species = db.Column(db.String(50), nullable=False)  # Species of the pet
    photo_url = db.Column(db.String(500), nullable=True)  # URL of the pet's photo
    age = db.Column(db.Integer, nullable=True)  # Age of the pet
    notes = db.Column(db.String(500), nullable=True)  # Additional notes about the pet
    available = db.Column(db.Boolean, nullable=False, default=True)  # Availability status of the pet
