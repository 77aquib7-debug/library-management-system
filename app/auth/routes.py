from flask import Blueprint

from flask import (render_template, request,redirect, url_for,flash,session)

from werkzeug.security import ( generate_password_hash,check_password_hash)

from app.models import User

from app.extensions import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method=="POST":
        
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User.query.filter_by(
            email=email
        ).first()
        
        if not user:
            flash("Invalid Credentials")
            return redirect(url_for("auth.login"))
        if not check_password_hash(
            user.password_hash, password
        ):
            flash("Invalid credentials")
            return redirect(url_for("auth.login"))
        if not user.active:
            flash("Account is deactivated")
            return redirect(url_for("auth.login"))
        
        if (user.role=="librarian" and not user.approved):
            flash("Account pending approval")
            return redirect(url_for("auth.login"))
        
        session["user_id"] = user.id
        
        
        if user.role=="admin":
            return "Admin Login Success"
        elif user.role=="librarian":
            return "Librarian Login Success"
            
        else:
            return "User Login Success"      
    
    return render_template(
        "auth/login.html"
    )
    
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    
    if request.method == "POST":
        
        name= request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")
        role=request.form.get("role")
        
        existing_user = User.query.filter_by(
            email=email
        ).first()
        
        if existing_user:
            flash(
                "Email already registered"
            )
            
            return redirect(
                url_for("auth.register")
        
            ) 
        
        if role not in [ "user", "librarian"]:
            flash("Invalid role")
            
            return redirect(
                url_for("auth.register")
            )
        
        approved=True
        
        if role=="librarian":
            approved= False
        
        new_user = User(
            name=name,
            email=email,
            password_hash=generate_password_hash(password),
            role=role,
            approved=approved,
            active=True
        )
        
        db.session.add(new_user)
        
        db.session.commit()
        
        flash("Registration Successful. Please login")        
        
        return redirect(
            url_for("auth.login")
        )
    else:
        return render_template("auth/register.html")   

@auth_bp.route("/logout")
def logout():
    
    if "user_id" not in session:
        flash("Please login first")
        return redirect(url_for("auth.login"))
    else:
        session.pop("user_id", None)
        
        flash("Logged out successfully.")
        
        return redirect(
            url_for("auth.login")
        )                      