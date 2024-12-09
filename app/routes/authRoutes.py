from flask import Blueprint, jsonify, request
import jwt
from datetime import datetime, timedelta

auth_routes = Blueprint('auth_routes', __name__)

# Secret key for encoding JWT token
SECRET_KEY = 'your_secret_key'

# Login route to generate JWT token
@auth_routes.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Here you can validate the email and password against the database
    if email == 'admin@example.com' and password == 'password123':  # Example check
        # Create JWT token
        expiration = datetime.utcnow() + timedelta(hours=1)  # Token valid for 1 hour
        token = jwt.encode({
            'email': email,
            'role': 'admin',  # Assign role for the user
            'exp': expiration
        }, SECRET_KEY, algorithm='HS256')

        return jsonify({'token': token})

    return jsonify({'message': 'Invalid credentials'}), 401
