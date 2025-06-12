import logging
from flask import Blueprint, jsonify, request
from app.models import FitnessClass
from datetime import datetime
import pytz
from app.timezone import convert_to_timezone


logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)

classes_bp = Blueprint('classes', __name__)

@classes_bp.route("", methods=["GET"])
def get_classes():
    user_tz_name = request.args.get("tz", "Asia/Kolkata")
    logger.info(f"Received request for classes with timezone: {user_tz_name}")

   
    try:
        user_tz = pytz.timezone(user_tz_name)
    except pytz.UnknownTimeZoneError:
        logger.warning(f"Invalid timezone provided: {user_tz_name}")
        return jsonify({"error": "Invalid timezone"}), 400

   
    date_str = request.args.get("date")
    if date_str:
        logger.info(f"Filtering classes by date: {date_str}")
        try:
            target_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            logger.error("Invalid date format provided.")
            return jsonify({"error": "Date must be in YYYY-MM-DD format"}), 400

        start = user_tz.localize(datetime.combine(target_date, datetime.min.time()))
        end = user_tz.localize(datetime.combine(target_date, datetime.max.time()))

        start_utc = start.astimezone(pytz.UTC)
        end_utc = end.astimezone(pytz.UTC)

        classes = FitnessClass.query.filter(
            FitnessClass.datetime >= start_utc,
            FitnessClass.datetime <= end_utc
        ).all()
    else:
        now_utc = datetime.utcnow().replace(tzinfo=pytz.UTC)
        logger.info("Fetching all upcoming classes from current UTC time.")
        classes = FitnessClass.query.filter(FitnessClass.datetime >= now_utc).all()

   
    result = []
    for cls in classes:
        localized_dt = convert_to_timezone(cls.datetime, user_tz_name)
        result.append({
            "id": cls.id,
            "name": cls.name,
            "instructor": cls.instructor,
            "datetime": localized_dt,
            "available_slots": cls.available_slots
        })

    logger.info(f"Returning {len(result)} classes.")
    return jsonify(result), 200
