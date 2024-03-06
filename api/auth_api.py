from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from app import db  # This should be replaced with actual import from your database module

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        user = AuthService.create_user(email=data['email'], password=data['password'])
        return jsonify(user.to_dict()), 201  # Respond with the new user's data, excluding the password hash
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = AuthService.verify_user(email=data['email'], password=data['password'])
    if user:
        return jsonify({'message': 'Logged in successfully'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401