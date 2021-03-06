"""Flask app for adopt app."""

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def index():
    """Display homepage with list of all pets."""

    pets = Pet.query.all()

    return render_template('index.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def pet_add():
    """Show AddPet form on GET request. If validated, add new pet to db
        and redirect to homepage."""

    form = AddPetForm()

    if form.validate_on_submit():

        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("pet_add.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def pet_page(pet_id):
    #TODO: say what happens if not valid
    """Show specific pet's details on page along with EditPet form on GET request.
        If validated, update pet's info in db and redirect back to homepage."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

#TODO: flash added hoorah
        return redirect("/")

    else:
        return render_template("pet_page.html", pet=pet, form=form)
