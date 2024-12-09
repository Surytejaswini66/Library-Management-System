from flask import Blueprint, jsonify
from utils.authentication import jwt_required

book_routes = Blueprint('book_routes', __name__)

# Example protected route to get the list of books
@book_routes.route('/books', methods=['GET'])
@jwt_required()  # Protect this route with JWT
def get_books():
    # Example data for the list of books
    books = [
        {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"id": 3, "title": "1984", "author": "George Orwell"}
    ]
    return jsonify({'books': books})

# Example protected route for adding a new book (admin only)
@book_routes.route('/books', methods=['POST'])
@jwt_required(role='admin')  # Protect this route and require admin role
def add_book():
    # Logic for adding a new book
    return jsonify({"message": "Book added successfully!"}), 201
