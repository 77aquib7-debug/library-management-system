from flask import Flask
from app.extensions import db
from app.extensions import migrate
from config import Config

def create_app():
    
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    
    migrate.init_app(app, db)
    
    from app import models
    
    return app