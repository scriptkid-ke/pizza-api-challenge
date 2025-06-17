from server.app import db

class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(
        db.Integer,
        db.ForeignKey("restaurants.id"),
        nullable=False
    )
    pizza_id = db.Column(
        db.Integer,
        db.ForeignKey("pizzas.id"),
        nullable=False
    )

    restaurant = db.relationship("Restaurant", back_populates="pizzas")
    pizza = db.relationship("Pizza", back_populates="restaurants")

    def to_dict(self, minimal=False):
        base = {"id": self.id, "price": self.price}
        if minimal:
            # used when nested under Restaurant
            base.update({"pizza_id": self.pizza_id})
        else:
            base.update({
                "pizza_id": self.pizza_id,
                "restaurant_id": self.restaurant_id,
                "pizza": self.pizza.to_dict(),
                "restaurant": {
                    "id": self.restaurant.id,
                    "name": self.restaurant.name,
                    "address": self.restaurant.address
                }
            })
        return base

    @staticmethod
    def validate_price(price):
        return 1 <= price <= 30
