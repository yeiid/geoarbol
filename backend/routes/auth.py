from flask import Blueprint, render_template, request, redirect, url_for, flash
from backend.database import db
from backend.models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    if User.query.filter_by(email=email).first():
        flash("El correo ya está registrado.", "error")
        return redirect(url_for("register_page"))

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    flash("Registro exitoso, inicia sesión.", "success")
    return redirect(url_for("login_page"))

@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    user = User.query.filter_by(email=email, password=password).first()

    if not user:
        flash("Credenciales incorrectas.", "error")
        return redirect(url_for("login_page"))

    flash("Inicio de sesión exitoso.", "success")
    return redirect(url_for("profile_page"))
