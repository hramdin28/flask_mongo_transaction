from flask import Blueprint
from flask_restx import Api

from app.main.teams.controller.team_controller import api as team_api

teams_bp = Blueprint(
    'teams_bp', __name__
)
api = Api(teams_bp, title="Teams api", version="1.0", description="Teams RESTX API")
api.add_namespace(team_api, path="/team_api")
