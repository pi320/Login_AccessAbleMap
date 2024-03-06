from utils.security import hash_password, check_password
from models.user import User
from app import db 

class AuthService:
    @staticmethod
    def create_user(email, password):
        # Check if user already exists
        if User.query.filter_by(user_email=email).first():
            raise ValueError('User already exists with that email.')

        # Create new user instance
        new_user = User(user_email=email)
        new_user.password_hash = hash_password(password)

        # Add new user to the database
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def verify_user(email, password):
        user = User.query.filter_by(user_email=email).first()   # Retrieve user by email

        # Check provided password against stored hash
        if user and check_password(user.password_hash, password):
            return user

        return None  # Return None if user doesn't exist or password doesn't match
