from flask import Blueprint, render_template, request
from backend.database import db
from backend.models import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/profile/<int:user_id>")
def profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return "Usuario no encontrado", 404
    return render_template("profile.html", user=user)

@user_bp.route("/profile/update", methods=["POST"])
def update_profile():
    user_id = request.form["user_id"]
    new_username = request.form["username"]

    user = User.query.get(user_id)
    if user:
        user.username = new_username
        db.session.commit()
    return "Perfil actualizado", 200
