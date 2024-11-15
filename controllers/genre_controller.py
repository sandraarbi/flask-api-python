from flask import jsonify, request
from models.models import db, Genre

def get_genres():
    genres = Genre.query.all()
    results = [genre.to_dict() for genre in genres]
    return jsonify(results)

def get_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if not genre:
        return jsonify({'message': 'Genre not found'}), 404
    return jsonify(genre.to_dict())

def add_genre():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'message': 'Invalid data'}), 400
    new_genre = Genre(name=data['name'])
    db.session.add(new_genre)
    db.session.commit()
    return jsonify(new_genre.to_dict()), 201

def update_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if not genre:
        return jsonify({'message': 'Genre not found'}), 404
    data = request.get_json()
    genre.name = data.get('name', genre.name)
    db.session.commit()
    return jsonify(genre.to_dict())

def delete_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if not genre:
        return jsonify({'message': 'Genre not found'}), 404
    db.session.delete(genre)
    db.session.commit()
    return jsonify({'message': 'Genre deleted successfully'})
