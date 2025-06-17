from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

rp_bp = Blueprint("restaurant_pizzas", __name__, url_prefix="/restaurant_pizzas")

@rp_bp.route("", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get("price")
    res_id = data.get("restaurant_id")
    piz_id = data.get("pizza_id")

    errors = []
    if price is None or not RestaurantPizza.validate_price(price):
        errors.append("Price must be between 1 and 30")
    if not Restaurant.query.get(res_id):
        errors.append("Restaurant not found")
    if not Pizza.query.get(piz_id):
        errors.append("Pizza not found")

    if errors:
        return jsonify(errors=errors), 400

    rp = RestaurantPizza(price=price,
                         restaurant_id=res_id,
                         pizza_id=piz_id)
    db.session.add(rp)
    db.session.commit()
    return jsonify(rp.to_dict()), 201
