from flask import Flask

def create_app(config: dict | None = None) -> Flask:
    app = Flask(__name__)

    # default config
    app.config.update(
        JSON_SORT_KEYS=False,  # keep JSON keys in insertion order (nicer for APIs)
    )

    # allow overrides (e.g., testing)
    if config:
        app.config.update(config)

    # register routes without circular imports
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
