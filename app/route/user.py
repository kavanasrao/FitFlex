from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging

user_bp = Blueprint('user', __name__)


logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    current_user_email = get_jwt_identity()
    logger.info(f"Authenticated access by: {current_user_email}")
    return jsonify({"message": "You are logged in", "email": current_user_email}), 200
