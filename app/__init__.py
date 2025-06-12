from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    load_dotenv()

    app = Flask(__name__)

    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///app.db")
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "super-secret-key")
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret")

    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)

   
    from app.models import user, FitnessClass, booking

 
    from app.route.auth import auth_bp
    from app.route.user import user_bp
    from app.route.classes import classes_bp
    from app.route.booking import booking_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(classes_bp, url_prefix='/classes')
    app.register_blueprint(booking_bp, url_prefix='/booking')

    return app
