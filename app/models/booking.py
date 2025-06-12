from datetime import datetime
from app import db


class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('fitness_classes.id'), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    client_email = db.Column(db.String(100), nullable=False)
    booked_at = db.Column(db.DateTime, default=datetime.utcnow)

    fitness_class = db.relationship('FitnessClass', back_populates='bookings')


    def __repr__(self):
        return f"<Booking {self.client_email} for class {self.class_id}>"