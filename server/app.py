from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


@app.route("/")
def home():
    return { "message": "Pizza API running!" }


def create_app():
    app = Flask(__name__)
    app.config.from_object("server.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    # import models so migrations detect them
    from server.models import restaurant, pizza, restaurant_pizza
    # register controllers/blueprints
    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    from server.controllers.restaurant_pizza_controller import rp_bp

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(rp_bp)

    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error="Not found"), 404

    return app

# for flask CLI
app = create_app()
