"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
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
