from flask_restx import Namespace, fields


class TeamApi:
    api = Namespace('Team', description='Team related operations')

    team_model = api.model('team', {
        'id': fields.String(),
        'name': fields.String(required=True, example='team x', max_length=20),
        'value': fields.Float(required=True),
        'current_tax_payed': fields.Float(required=True),
        'players': fields.List(fields.String()),
    }, strict=True)
