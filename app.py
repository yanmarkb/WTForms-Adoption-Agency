from flask import Flask, render_template, request, redirect, url_for, session, flash  # Import necessary modules from Flask.
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for database operations.
from flask_debugtoolbar import DebugToolbarExtension  # Import DebugToolbarExtension for debugging.
from models import db, Pet  # Import the database and Pet model.
from forms import AddPetForm, EditPetForm  # Import the forms for adding and editing pets.

app = Flask(__name__)  # Create a Flask application.

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'  # Set the database URI.
app.config['SQLALCHEMY_ECHO'] = True  # Enable echoing SQL statements.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications.
app.config['SECRET_KEY'] = "secret"  # Set the secret key for session encryption.
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False  # Disable DebugToolbar redirect interception.

debug = DebugToolbarExtension(app)  # Initialize the DebugToolbar.

db.init_app(app)  # Initialize the database.

@app.before_first_request
def create_tables():
    """
    Create database tables before the first request is handled.
    """
    db.create_all()  # Create all the database tables.

@app.route('/')
def homepage():
    """
    Render the homepage template with all the pets.
    """
    pets = Pet.query.all()  # Retrieve all the pets from the database.
    return render_template('home.html', pets=pets)  # Render the homepage template with the pets.

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """
    Add a new pet to the database.
    """
    form = AddPetForm()  # Create an instance of the AddPetForm.

    if form.validate_on_submit():
        name = form.name.data  # Get the name of the pet from the form.
        species = form.species.data  # Get the species of the pet from the form.
        photo_url = form.photo_url.data  # Get the photo URL of the pet from the form.
        age = form.age.data  # Get the age of the pet from the form.
        notes = form.notes.data  # Get the notes of the pet from the form.

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)  # Create a new Pet object with the form data.
        db.session.add(new_pet)  # Add the new pet to the database session.
        db.session.commit()  # Commit the changes to the database.

        return redirect(url_for('homepage'))  # Redirect to the homepage.

    return render_template('add_pet.html', form=form)  # Render the add_pet template with the form.

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_and_edit_pet(pet_id):
    """
    Show and edit the details of a specific pet.
    """
    pet = Pet.query.get_or_404(pet_id)  # Retrieve the pet with the given ID from the database.
    form = EditPetForm(obj=pet)  # Create an instance of the EditPetForm with the pet data.

    if form.validate_on_submit():
        form.populate_obj(pet)  # Update the pet object with the form data.
        db.session.commit()  # Commit the changes to the database.
        return redirect(url_for('homepage'))  # Redirect to the homepage.

    return render_template('show_and_edit_pet.html', form=form, pet=pet)  # Render the show_and_edit_pet template with the form and pet.

@app.route('/delete_pet/<int:pet_id>', methods=["POST"])
def delete_pet(pet_id):
    """
    Delete a pet from the database.
    """
    pet = Pet.query.get_or_404(pet_id)  # Retrieve the pet with the given ID from the database.
    db.session.delete(pet)  # Delete the pet from the database.
    db.session.commit()  # Commit the changes to the database.
    return redirect(url_for('homepage'))  # Redirect to the homepage.

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask application in debug mode.
