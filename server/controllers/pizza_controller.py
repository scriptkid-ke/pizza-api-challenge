from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint("pizzas", __name__, url_prefix="/pizzas")

@pizza_bp.route("", methods=["GET"])
def get_pizzas():
    all_p = Pizza.query.all()
    return jsonify([p.to_dict() for p in all_p]), 200
