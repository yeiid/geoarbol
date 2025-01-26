from flask import Flask, render_template
from backend.routes.auth import auth_bp
from backend.routes.user import user_bp
from backend.routes.trees import trees_bp
from backend.database import db
from backend.config import Config

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
app.config.from_object(Config)

db.init_app(app)

# Registrar Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(trees_bp, url_prefix="/trees")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/profile")
def profile_page():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
