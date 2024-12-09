@borrow_routes.route("/borrow-requests/<int:id>/approve", methods=["PUT"])
@jwt_required(role="librarian")
def approve_borrow_request(id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("UPDATE borrow_requests SET status = 'Approved' WHERE id = ?", (id,))
    db.commit()
    return jsonify({'message': 'Request approved'}), 200
@borrow_routes.route("/borrow-requests", methods=["POST"])
@jwt_required(role="user")
def create_borrow_request():
    data = request.get_json()
    user_id = data['user_id']
    book_id = data['book_id']
    start_date = data['start_date']
    end_date = data['end_date']

    db = get_db()
    cursor = db.cursor()

    cursor.execute('INSERT INTO borrow_requests (user_id, book_id, start_date, end_date, status) VALUES (?, ?, ?, ?, ?)',
                   (user_id, book_id, start_date, end_date, 'Pending'))
    db.commit()

    return jsonify({'message': 'Borrow request created successfully'}), 201
