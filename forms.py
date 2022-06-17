"""Forms for adopt app."""

from wsgiref.validate import validator
from matplotlib.style import available
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    # TODO: add form validation
    name = StringField('Pet Name',
                       validators=[InputRequired()])
    species = SelectField('Species',
                          choices=[
                              ('cat', 'Cat'),
                              ('dog', 'Dog'),
                              ('porcupine', 'Porcupine')],
                          validators=[InputRequired()])
    photo_url = StringField('Photo URL',
                            validators=[Optional(), URL()])
    age = SelectField('Age',
                      choices=[
                          ('baby', 'Baby'),
                          ('young', 'Young'),
                          ('adult', 'Adult'),
                          ('senior', 'Senior')],
                      # do we need this inputrequired validator for age?
                      validators=[InputRequired()])
    notes = TextAreaField('Additional notes',
                          validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing pet."""

    photo_url = StringField('Photo URL',
                            validators=[Optional(), URL()])

    notes = TextAreaField('Additional notes',
                          validators=[Optional()])

    available = BooleanField('Available', 
                            validators=[Optional()])
