from app import create_app, db
from app.models import User, FitnessClass, Booking
from flask import jsonify  

app = create_app()


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Fitness Class Booking API"}), 200

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'FitnessClass': FitnessClass,
        'Booking': Booking
    }

if __name__ == '__main__':
    app.run(debug=True)
