from flask import Flask
from app.extensions import db
from app.extensions import migrate
from config import Config
from app.auth.routes import auth_bp
from app.admin.routes import admin_bp
from app.librarian.routes import librarian_bp
from app.user.routes import user_bp

def create_app():
    
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    
    migrate.init_app(app, db)
    
    from app import models
    
    app.register_blueprint(auth_bp)
    
    app.register_blueprint(admin_bp)
    
    app.register_blueprint(librarian_bp)
    
    app.register_blueprint(user_bp)
    
    return app