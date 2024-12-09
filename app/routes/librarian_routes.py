from flask import Blueprint, request, jsonify
from app.controllers.librarian import add_book

librarian_routes = Blueprint('librarian', __name__)

@librarian_routes.route('/add-book', methods=['POST'])
def add_book_route():
    data = request.get_json()
    title = data['title']
    author = data['author']
    quantity = data['quantity']
    response = add_book(title, author, quantity)
    return jsonify(response)
