import pytest
from bson import ObjectId

from app.main.teams import TEAM_API
from app.main.teams.dto.team_dto import TeamDto


@pytest.fixture
def mock_team() -> TeamDto:
    doc_id = ObjectId()
    return TeamDto(id=str(doc_id), name='team1', value=200)


def test_team_get(client, mocker, mock_team):
    mocker.patch('app.main.teams.service.impl.team_service_football.team_service_football.get_all',
                 return_value=[mock_team])
    response = client.get(f"{TEAM_API}/")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == mock_team.id
    assert response.json[0]['name'] == mock_team.name
    assert response.json[0]['value'] == mock_team.value


def test_team_post(client, mocker, mock_team):
    mocker.patch('app.main.teams.service.impl.team_service_football.team_service_football.create',
                 return_value=mock_team)
    response = client.post(f"{TEAM_API}/", json=mock_team)
    assert response.status_code == 200
    assert response.json['id'] == mock_team.id
    assert response.json['name'] == mock_team.name
    assert response.json['value'] == mock_team.value


def test_team_put(client, mocker, mock_team):
    mocker.patch('app.main.teams.service.impl.team_service_football.team_service_football.update',
                 return_value=mock_team)
    response = client.put(f"{TEAM_API}/", json=mock_team)
    assert response.status_code == 200
    assert response.json['id'] == mock_team.id
    assert response.json['name'] == mock_team.name
    assert response.json['value'] == mock_team.value


def test_team_by_id_delete(client, mocker, mock_team):
    mocker.patch('app.main.teams.service.impl.team_service_football.team_service_football.delete',
                 return_value=True)
    response = client.delete(f"{TEAM_API}/{str(mock_team.id)}")
    assert response.status_code == 200
    assert response.json
