from flask_wtf import FlaskForm  # Importing the FlaskForm class from the flask_wtf module.
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField  # Importing specific fields from the wtforms module.
from wtforms.validators import Optional, Length, URL, NumberRange  # Importing specific validators from the wtforms.validators module.

class AddPetForm(FlaskForm):
    """
    Form for adding a pet.
    """
    name = StringField('Pet Name', [Length(min=1, max=100)])  # Creating a StringField for the pet's name with a length validator.
    species = StringField('Species', [Length(min=1, max=100)])  # Creating a StringField for the pet's species with a length validator.
    photo_url = StringField('Photo URL', [Optional(), URL()])  # Creating a StringField for the pet's photo URL with optional and URL validators.
    age = IntegerField('Age', [Optional(), NumberRange(min=0, max=30)])  # Creating an IntegerField for the pet's age with optional and number range validators.
    notes = TextAreaField('Notes', [Optional(), Length(max=500)])  # Creating a TextAreaField for the pet's notes with optional and length validators.

class EditPetForm(FlaskForm):
    """
    Form for editing a pet.
    """
    photo_url = StringField('Photo URL', [Optional(), URL()])  # Creating a StringField for the pet's photo URL with optional and URL validators.
    notes = TextAreaField('Notes', [Optional(), Length(max=500)])  # Creating a TextAreaField for the pet's notes with optional and length validators.
    available = BooleanField('Available')  # Creating a BooleanField to indicate if the pet is available.
