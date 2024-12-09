from flask import Blueprint, request, jsonify
from app.controllers.user import borrow_book

user_routes = Blueprint('user', __name__)

@user_routes.route('/borrow-book', methods=['POST'])
def borrow_book_route():
    data = request.get_json()
    user_id = data['user_id']
    book_id = data['book_id']
    response = borrow_book(user_id, book_id)
    return jsonify(response)
