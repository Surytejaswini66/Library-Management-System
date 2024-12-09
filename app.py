from flask import Flask, request, jsonify
from utils.authentication import generate_token, jwt_required
from utils.csv_export import export_to_csv

app = Flask(__name__)

# Example User Data (replace with DB in production)
@app.route('/api/users/<int:user_id>/history/csv', methods=['GET'])
@jwt_required(role="user")
def download_borrow_history(user_id):
    # Example data; replace with actual DB query
    history = [
        {"book_title": "Book 1", "borrowed_on": "2024-12-01", "returned_on": "2024-12-10"},
        {"book_title": "Book 2", "borrowed_on": "2024-12-15", "returned_on": None}
    ]
    return export_to_csv(history, "borrow_history")
users = {
    "librarian@example.com": {"password": "password123", "role": "librarian"},
    "user@example.com": {"password": "password123", "role": "user"}
}
print("Starting Flask application...")
app.run(debug=True)

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = users.get(email)
    if user and user['password'] == password:
        token = generate_token(email, user['role'])
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid credentials"}), 401
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'message': 'Books endpoint works!'})
if __name__ == "__main__":
    app.run(debug=False)
