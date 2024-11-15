from config import db

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    developer_id = db.Column(db.Integer, db.ForeignKey('developers.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
            'developer_id': self.developer_id,
            'genre_id': self.genre_id
        }

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Developer(db.Model):
    __tablename__ = 'developers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
