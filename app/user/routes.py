from flask import Blueprint
from app.utils.decorators import role_required





user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/dashboard")
@role_required("user")
def dashboard():
    return "User Dashboard"