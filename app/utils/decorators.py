from functools import wraps
from app.models import User

from flask import (
    session, flash, redirect, url_for
)

def login_required(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        if "user_id" not in session:
            
            flash("Please login first.")
            return redirect(
                url_for("auth.login")
            )
        return func(*args, **kwargs)    
    return wrapper


      

def role_required(required_role):
    def decorator(func):
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            if "user_id" not in session:
                flash("Please login first.")
                return redirect(url_for("auth.login"))
            
            user = User.query.get(session["user_id"])
            if not user:
                flash("User not found.")
                return redirect(url_for("auth.login"))
            
            if not user.active:
                flash("Account deactivated.")
                return redirect(url_for("auth.login")) 
            
            if user.role != required_role:
                flash("Access denied.")
                
                return redirect(url_for("auth.login"))
            return func(*args,**kwargs)
        return wrapper
    return decorator