from flask import jsonify, request
from models.models import db, Developer

def get_developers():
    developers = Developer.query.all()
    results = [developer.to_dict() for developer in developers]
    return jsonify(results)

def get_developer(developer_id):
    developer = Developer.query.get(developer_id)
    if not developer:
        return jsonify({'message': 'Developer not found'}), 404
    return jsonify(developer.to_dict())

def add_developer():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'message': 'Invalid data'}), 400
    new_developer = Developer(name=data['name'])
    db.session.add(new_developer)
    db.session.commit()
    return jsonify(new_developer.to_dict()), 201

def update_developer(developer_id):
    developer = Developer.query.get(developer_id)
    if not developer:
        return jsonify({'message': 'Developer not found'}), 404
    data = request.get_json()
    developer.name = data.get('name', developer.name)
    db.session.commit()
    return jsonify(developer.to_dict())

def delete_developer(developer_id):
    developer = Developer.query.get(developer_id)
    if not developer:
        return jsonify({'message': 'Developer not found'}), 404
    db.session.delete(developer)
    db.session.commit()
    return jsonify({'message': 'Developer deleted successfully'})
