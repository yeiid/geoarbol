from flask import Blueprint, request, jsonify
from backend.database import db
from backend.models.tree import Tree

trees_bp = Blueprint("trees", __name__)

@trees_bp.route("/", methods=["POST"])
def add_tree():
    data = request.json
    tree = Tree(name=data["name"], species=data["species"], latitude=data["latitude"], longitude=data["longitude"], user_id=data["user_id"])
    db.session.add(tree)
    db.session.commit()
    return jsonify({"message": "Árbol registrado"}), 201

@trees_bp.route("/<int:user_id>", methods=["GET"])
def get_trees(user_id):
    trees = Tree.query.filter_by(user_id=user_id).all()
    return jsonify([{"name": t.name, "species": t.species, "lat": t.latitude, "lon": t.longitude} for t in trees]), 200
