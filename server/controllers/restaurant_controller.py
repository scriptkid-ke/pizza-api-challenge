from flask import Blueprint, request, jsonify
from server.models.restaurant import Restaurant
from server.app import db

restaurant_bp = Blueprint("restaurants", __name__, url_prefix="/restaurants")

@restaurant_bp.route("", methods=["GET"])
def get_restaurants():
    all_r = Restaurant.query.all()
    return jsonify([r.to_dict() for r in all_r]), 200

@restaurant_bp.route("/<int:id>", methods=["GET"])
def get_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify(error="Restaurant not found"), 404
    return jsonify(r.to_dict()), 200

@restaurant_bp.route("/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify(error="Restaurant not found"), 404
    db.session.delete(r)
    db.session.commit()
    return "", 204
