"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Model schema for Pet."""

    __tablename__ = 'pets'

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
        default='')
    age = db.Column(
        db.Text,
        nullable=false)
    notes = db.Column(
        db.Text)
    available = db.Column(
        db.Boolean,
        nullable=false,
        default=True)
