from flask import Blueprint
# app/routes/csvRoutes.py
from app.controllers.csvController import export_books_to_csv

csv_routes = Blueprint("csv_routes", __name__)

csv_routes.route("/export/csv", methods=["GET"])(export_books_to_csv)
# app/routes/csvRoutes.py
from app.controllers.csvController import export_books_to_csv

# Example route using the function
@csv_routes.route('/export', methods=['GET'])
def export_books():
    export_books_to_csv()
    return "Books exported successfully"
