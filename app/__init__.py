from flask import Flask
from app.routes.librarian_routes import librarian_routes
from app.routes.user_routes import user_routes

def create_app():
    app = Flask(__name__)

    # Register the blueprints
    app.register_blueprint(librarian_routes, url_prefix='/api/librarian')
    app.register_blueprint(user_routes, url_prefix='/api/user')

    return app
