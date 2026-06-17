from flask import Blueprint
from app.utils.decorators import (role_required, login_required)




admin_bp = Blueprint("admin",__name__, url_prefix="/admin")




@admin_bp.route("/dashboard")
@role_required("admin")
def dashboard():
    return "Admin Dashboard"
