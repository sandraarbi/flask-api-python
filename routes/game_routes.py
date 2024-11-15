from flask import Blueprint
from controllers.game_controller import get_games, get_game, add_game, update_game, delete_game

game_bp = Blueprint('game_bp', __name__)

# Routes for games
game_bp.route('/api/games', methods=['GET'])(get_games)
game_bp.route('/api/games/<int:game_id>', methods=['GET'])(get_game)
game_bp.route('/api/games', methods=['POST'])(add_game)
game_bp.route('/api/games/<int:game_id>', methods=['PUT'])(update_game)
game_bp.route('/api/games/<int:game_id>', methods=['DELETE'])(delete_game)
