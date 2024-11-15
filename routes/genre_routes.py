from flask import Blueprint
from controllers.genre_controller import get_genres, get_genre, add_genre, update_genre, delete_genre

# Blueprint for genre routes
genre_bp = Blueprint('genre_bp', __name__)

# Routes for genres
genre_bp.route('/api/genres', methods=['GET'])(get_genres)          # Get all genres
genre_bp.route('/api/genres/<int:genre_id>', methods=['GET'])(get_genre)  # Get a specific genre by ID
genre_bp.route('/api/genres', methods=['POST'])(add_genre)          # Add a new genre
genre_bp.route('/api/genres/<int:genre_id>', methods=['PUT'])(update_genre)  # Update an existing genre
genre_bp.route('/api/genres/<int:genre_id>', methods=['DELETE'])(delete_genre)  # Delete a genre by ID
