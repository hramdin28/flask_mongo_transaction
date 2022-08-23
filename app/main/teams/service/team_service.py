from abc import ABC, abstractmethod

from app.main.teams.dto.team_dto import TeamDto
from app.main.teams.model.team import Team


class TeamService(ABC):
    @abstractmethod
    def get_all(self) -> [TeamDto]:
        pass

    def team_to_dto(self, team: Team) -> TeamDto:
        return TeamDto(
            id=str(team.id),
            name=team.name,
            value=team.value)
