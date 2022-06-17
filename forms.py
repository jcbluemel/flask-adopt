"""Forms for adopt app."""

from wsgiref.validate import validator
# TODO: why error with this not commented out?
# from matplotlib.style import available
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pet."""

    name = StringField(
        'Pet Name',
        validators=[InputRequired()])

    species = SelectField(
        'Species',
        choices=[
            ('cat', 'Cat'),
            ('dog', 'Dog'),
            ('porcupine', 'Porcupine')],
        validators=[InputRequired()])

    photo_url = StringField(
        'Photo URL',
        validators=[Optional(), URL()])

    age = SelectField(
        'Age',
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')],
        validators=[InputRequired()])

    notes = TextAreaField(
        'Additional notes',
        validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing pet details."""

    photo_url = StringField(
        'Photo URL',
        validators=[Optional(), URL()])

    notes = TextAreaField(
        'Additional notes',
        validators=[Optional()])

    available = BooleanField(
        'Available',
        validators=[Optional()])
