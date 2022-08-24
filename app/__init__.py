from flask import Flask
from flask_mongoengine import MongoEngine
from flask_principal import Principal

from config import config_by_profile

# Globally accessible libraries
db = MongoEngine()


def create_app(profile: str):
    print(f"Profile: {profile}")
    app = Flask(__name__)
    app.config.from_object(config_by_profile[profile])
    db.init_app(app)
    with app.app_context():
        app._principal = Principal(app, use_sessions=False)
        from .main.teams import teams_bp as teams_bp
        app.register_blueprint(teams_bp)
    return app
