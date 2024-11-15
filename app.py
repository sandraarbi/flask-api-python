from config import create_app, db
from routes.game_routes import game_bp
from routes.genre_routes import genre_bp
from routes.developer_routes import developer_bp

# Membuat aplikasi menggunakan create_app
app = create_app()

# Register blueprint
app.register_blueprint(game_bp)
app.register_blueprint(genre_bp)
app.register_blueprint(developer_bp)

# Membuat tabel di database jika belum ada
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
