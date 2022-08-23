from dataclasses import dataclass

from bson import ObjectId
from pymongo.results import InsertOneResult, DeleteResult

from app.main.teams.model.team import Team
from app.main.teams.wrapper.transaction_wrapper import TRANSACTION_DB, TRANSACTION_SESSION


@dataclass(repr=False, eq=False)
class TeamRepository:
    collection = 'team'

    def fetch_all(self) -> [Team]:
        return Team.objects

    def find_by_id(self, doc_id: str) -> Team:
        return Team.objects.get(id=doc_id)

    def save(self, team: Team, **kwargs) -> Team:
        result: InsertOneResult = kwargs.get(TRANSACTION_DB).get_collection(self.collection).insert_one(
            team.to_mongo(),
            session=kwargs.get(TRANSACTION_SESSION)
        )
        team.id = result.inserted_id
        return team

    def update(self, team: Team, **kwargs) -> Team:
        kwargs.get(TRANSACTION_DB).get_collection(self.collection).update_one(
            {"_id": team.id},
            {"$set": {'name': team.name, 'value': team.value}},
            session=kwargs.get(TRANSACTION_SESSION)
        )
        return team

    def delete(self, doc_id: str, **kwargs) -> bool:
        result: DeleteResult = kwargs.get(TRANSACTION_DB).get_collection(self.collection).delete_one(
            {"_id": ObjectId(doc_id)},
            session=kwargs.get(TRANSACTION_SESSION)
        )
        return result.deleted_count > 0


team_repository = TeamRepository()
