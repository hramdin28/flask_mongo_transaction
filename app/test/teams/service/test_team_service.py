import pytest

from app.main.teams.dto.team_dto import TeamDto
from app.main.teams.service.impl.team_service_football import team_service_football


@pytest.fixture
def create() -> TeamDto:
    team = TeamDto(id='', name='Team x', value=200)
    return team_service_football.create(team)


def test_save(mongo_db, create):
    result: TeamDto = create
    assert result.name == 'Team x'
    assert result.value == 200
    assert result.id != ''


def test_update(mongo_db, create):
    result_created: TeamDto = create
    result_created.value = 350

    result_updated: TeamDto = team_service_football.update(result_created)
    assert result_updated.name == result_created.name
    assert result_updated.value == result_created.value
    assert result_updated.id == result_created.id


def test_delete(mongo_db, create):
    result_created: TeamDto = create

    result_deleted: bool = team_service_football.delete(str(result_created.id))
    assert result_deleted


def test_get_all(mongo_db, create):
    result_created: TeamDto = create

    result = team_service_football.get_all()
    assert len(result) == 1
    assert result[0].id == result_created.id
