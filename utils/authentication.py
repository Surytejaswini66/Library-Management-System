from functools import wraps
from flask import request, jsonify
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"  # Change to a strong secret in production

def generate_token(user_id, role):
    """Generates a JWT token."""
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=1)  # 1-hour validity
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def jwt_required(role=None):
    """Decorator for routes that require JWT authentication."""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization', None)
            if not token:
                return jsonify({'message': 'Token is missing'}), 401

            try:
                decoded = jwt.decode(token.split(" ")[1], SECRET_KEY, algorithms=['HS256'])
                if role and decoded['role'] != role:
                    return jsonify({'message': 'Unauthorized'}), 403
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token expired'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 401

            request.user = decoded  # Attach user info to the request object
            return f(*args, **kwargs)
        return wrapper
    return decorator
