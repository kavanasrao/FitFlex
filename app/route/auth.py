from flask import Blueprint, request, jsonify
from app.models import db, User
from flask_jwt_extended import create_access_token
import logging

auth_bp = Blueprint('auth', __name__)


logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        logger.warning("Registration failed: Missing fields.")
        return jsonify({"error": "Missing fields"}), 400

    if User.query.filter_by(email=data['email']).first():
        logger.warning(f"Email already registered: {data['email']}")
        return jsonify({"error": "Email already registered"}), 400

    try:
        user = User(name=data['username'], email=data['email'])  
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()

        logger.info(f"User created successfully: {data['email']}")
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        logger.error(f"Registration error: {str(e)}")
        db.session.rollback()
        return jsonify({"error": "Server error"}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        logger.warning("Login failed: Missing credentials.")
        return jsonify({"error": "Missing credentials"}), 400

    try:
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            token = create_access_token(identity=user.email)
            logger.info(f"User logged in: {data['email']}")
            return jsonify(access_token=token), 200

        logger.warning(f"Login failed: Invalid credentials for {data['email']}")
        return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        return jsonify({"error": "Server error"}), 500