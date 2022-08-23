from flask import request
from flask_restx import Resource

from app.main.teams.api.team_api import TeamApi
from app.main.teams.dto.team_dto import TeamDto
from app.main.teams.service.impl.team_service_football import team_service_football

api = TeamApi.api
team_model = TeamApi.team_model


@api.route("/")
class Teams(Resource):
    @api.marshal_with(team_model)
    def get(self):
        return team_service_football.get_all()

    @api.expect(team_model, validate=True)
    @api.marshal_with(team_model)
    def post(self):
        req = request.get_json()
        return team_service_football.create(TeamDto(id="", name=req['name'], value=req['value']))

    @api.expect(team_model, validate=True)
    @api.marshal_with(team_model)
    def put(self):
        req = request.get_json()
        return team_service_football.update(TeamDto(id=req['id'], name=req['name'], value=req['value']))


@api.route('/<doc_id>')
@api.param('doc_id', 'The parameter identifier')
class TeamsById(Resource):

    def delete(self, doc_id):
        return team_service_football.delete(doc_id)
