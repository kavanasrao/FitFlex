from app import create_app
from app.models import db, FitnessClass, User, Booking
from datetime import datetime, timedelta
import pytz


app = create_app()
app.app_context().push()


db.drop_all()
db.create_all()


now = datetime.now(pytz.UTC)


classes = [
    FitnessClass(
        name="Morning Yoga",
        instructor="Anjali Mehra",
        datetime=now + timedelta(days=1, hours=7),
        available_slots=10
    ),
    FitnessClass(
        name="Evening Zumba",
        instructor="Rohan Kapoor",
        datetime=now + timedelta(days=2, hours=18),
        available_slots=8
    ),
    FitnessClass(
        name="Pilates Pro",
        instructor="Neha Sharma",
        datetime=now + timedelta(days=3, hours=9),
        available_slots=12
    )
]
db.session.add_all(classes)
db.session.commit()


user = User(
    name="Test User",
    email="testuser@example.com"
)
user.set_password("Test@1234")
db.session.add(user)
db.session.commit()


booking = Booking(
    class_id=classes[0].id,
    client_name="Test User",
    client_email="testuser@example.com"
)
classes[0].available_slots -= 1
db.session.add(booking)
db.session.commit()

print(" Database seeded successfully!")
