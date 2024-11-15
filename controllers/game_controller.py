from flask import jsonify, request
from models.models import db, Game

def get_games():
    games = Game.query.all()
    results = [game.to_dict() for game in games]
    return jsonify(results)

def get_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'message': 'Game not found'}), 404
    return jsonify(game.to_dict())

def add_game():
    data = request.get_json()
    if not data or not all(key in data for key in ('title', 'release_year', 'developer_id', 'genre_id')):
        return jsonify({'message': 'Invalid data'}), 400
    new_game = Game(
        title=data['title'],
        release_year=data['release_year'],
        developer_id=data['developer_id'],
        genre_id=data['genre_id']
    )
    db.session.add(new_game)
    db.session.commit()
    return jsonify(new_game.to_dict()), 201

def update_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'message': 'Game not found'}), 404
    data = request.get_json()
    game.title = data.get('title', game.title)
    game.release_year = data.get('release_year', game.release_year)
    game.developer_id = data.get('developer_id', game.developer_id)
    game.genre_id = data.get('genre_id', game.genre_id)
    db.session.commit()
    return jsonify(game.to_dict())

def delete_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'message': 'Game not found'}), 404
    db.session.delete(game)
    db.session.commit()
    return jsonify({'message': 'Game deleted successfully'})
