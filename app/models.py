from app.extensions import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "user"
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    approved = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    books = db.relationship("Book", back_populates="librarian")
    borrows = db.relationship("Borrow", back_populates="user")
class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(200), nullable=False)
    total_copies = db.Column(db.Integer, nullable=False)
    available_copies = db.Column(db.Integer, nullable=False)
    assigned_librarian_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    librarian = db.relationship("User", back_populates="books")
    borrows = db.relationship("Borrow", back_populates="book")

class Borrow(db.Model):
    __tablename__= "borrow"
    
    id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    borrow_date = db.Column(db.DateTime, default= datetime.utcnow)
    return_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), nullable=False, default="borrowed")
    user = db.relationship("User", back_populates="borrows")        
    book = db.relationship("Book", back_populates="borrows")        