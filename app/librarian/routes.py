from flask import Blueprint
from app.utils.decorators import role_required





librarian_bp = Blueprint("librarian",__name__, url_prefix="/librarian" )


@librarian_bp.route("/dashboard")
@role_required("librarian")
def dashboard():
    return "Librarian Dashboard"    