"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, false, CheckConstraint

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet."""

    __tablename__ = 'pets'

    #TODO: add to form checking
    # poss_ages = ['baby', 'young', 'adult', 'senior']

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)
    name = db.Column(
        db.String(50),
        nullable=false)
    species = db.Column(
        db.String(50),
        nullable=false)
    photo_url = db.Column(
        db.Text,
        nullable=false,
        default='')
    age = db.Column(
        db.Text,
        # db.CheckConstraint(f'age in {poss_ages}'),
        nullable=false)
    notes = db.Column(
        db.Text)
    available = db.Column(
        db.Boolean,
        nullable=false,
        default=True)

