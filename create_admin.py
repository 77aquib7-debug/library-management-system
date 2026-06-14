from app import create_app
from app.models import User
from app.extensions import db
from werkzeug.security import generate_password_hash


app = create_app()


with app.app_context():
    admin = User.query.filter_by(email= "admin@library.com",role="admin").first()
    
    if admin:
        print("Admin already exists.")
    
    else:
        admin = User(
            name = "Admin",
            email= "admin@library.com",
            password_hash = generate_password_hash("admin123"),
            role= "admin",
            approved=True,
            active=True
        )
        
        db.session.add(admin)
        db.session.commit()
        
        print("Admin created successfully.")
        