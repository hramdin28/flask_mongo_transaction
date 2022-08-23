from dataclasses import dataclass
from datetime import datetime

from dateutil import relativedelta

from app.main.teams.dto.team_dto import TeamDto
from app.main.teams.model.team import Team
from app.main.teams.repository.TeamRepository import TeamRepository, team_repository
from app.main.teams.service.team_service import TeamService
from app.main.teams.wrapper.transaction_wrapper import transactional


@dataclass(repr=False, eq=False)
class TeamServiceFootball(TeamService):
    team_repository: TeamRepository
    rate: float = 0.5

    def get_all(self) -> [TeamDto]:
        teams = self.team_repository.fetch_all()
        iterator = map(self.assign_tax, teams)
        return list(iterator)

    @transactional
    def create(self, team: TeamDto, **kwargs) -> TeamDto:
        model = Team(name=team.name, value=team.value)
        model = self.team_repository.save(model, **kwargs)
        return self.assign_tax(model)

    @transactional
    def update(self, team: TeamDto, **kwargs) -> TeamDto:
        model = self.team_repository.find_by_id(team.id)
        model.name = team.name
        model.value = team.value
        model = self.team_repository.update(model, **kwargs)
        return self.assign_tax(model)

    @transactional
    def delete(self, doc_id: str, **kwargs) -> bool:
        return self.team_repository.delete(doc_id, **kwargs)

    def assign_tax(self, team: Team) -> TeamDto:
        team_dto = self.team_to_dto(team)
        team_dto.current_tax_payed = self.calculate_yearly_pro_rata_tax(team)
        return team_dto

    def calculate_yearly_pro_rata_tax(self, team: Team) -> float:
        today = datetime.now()
        start_of_year = today.replace(month=1, day=1, hour=0, minute=0)
        delta = relativedelta.relativedelta(today, start_of_year)
        return ((team.value * self.rate) / 12) * delta.months


team_service_football = TeamServiceFootball(team_repository)
