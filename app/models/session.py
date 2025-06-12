from datetime import datetime
from app import db

class FitnessClass(db.Model):
    __tablename__ = 'fitness_classes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, index=True)
    available_slots = db.Column(db.Integer, nullable=False)

    bookings = db.relationship('Booking', back_populates='fitness_class', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<FitnessClass {self.name} at {self.datetime}>"
