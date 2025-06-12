import logging
from flask import Blueprint, request, jsonify
from app.models import db, FitnessClass, Booking
from flask_jwt_extended import jwt_required


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/book', methods=['POST'])
@jwt_required()
def book_class():
    data = request.get_json()
    class_id = data.get('class_id')
    client_name = data.get('client_name')
    client_email = data.get('client_email')

    logger.info(f"Booking request received: class_id={class_id}, client_name={client_name}, email={client_email}")

    if not all([class_id, client_name, client_email]):
        logger.warning("Booking failed: Missing fields in request.")
        return jsonify({"error": "Missing fields"}), 400

    fitness_class = FitnessClass.query.get(class_id)
    if not fitness_class:
        logger.warning(f"Booking failed: Class ID {class_id} not found.")
        return jsonify({"error": "Class not found"}), 404

    if fitness_class.available_slots <= 0:
        logger.info(f"Booking rejected: Class ID {class_id} is fully booked.")
        return jsonify({"error": "Class is fully booked"}), 400

    try:
        booking = Booking(
            class_id=class_id,
            client_name=client_name,
            client_email=client_email
        )
        fitness_class.available_slots -= 1
        db.session.add(booking)
        db.session.commit()
        logger.info(f"Booking successful: Class {class_id} by {client_email}")
        return jsonify({"message": "Booking successful"}), 201

    except Exception as e:
        db.session.rollback()
        logger.error(f"Booking failed: DB commit error - {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


@booking_bp.route('/bookings', methods=['GET'])
@jwt_required()
def get_bookings():
    email = request.args.get('email')
    if not email:
        logger.warning("Fetching bookings failed: Email not provided.")
        return jsonify({"error": "Email is required"}), 400

    logger.info(f"Fetching bookings for: {email}")
    try:
        bookings = Booking.query.filter_by(client_email=email).all()
        output = [{
            "class": b.fitness_class.name,
            "start_time": b.fitness_class.datetime.isoformat(),
            "client_name": b.client_name
        } for b in bookings]

        logger.info(f"Returned {len(output)} bookings for {email}")
        return jsonify(output), 200

    except Exception as e:
        logger.error(f"Error fetching bookings for {email}: {str(e)}")
        return jsonify({"error": "Could not fetch bookings"}), 500