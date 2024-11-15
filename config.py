from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Inisialisasi SQLAlchemy tanpa diikat ke aplikasi
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Konfigurasi database (gunakan nama db_movie)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dbgame_newspaper:4c772262a48079ef460dd3688ca4b2fc06239103@28vlu.h.filess.io:3307/dbgame_newspaper'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inisialisasi SQLAlchemy dengan aplikasi
    db.init_app(app)

    return app
