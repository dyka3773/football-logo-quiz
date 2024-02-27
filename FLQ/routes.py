from flask import Blueprint
import json

from utils import csv_loader
from models.Team import Team
from typing import List


bp = Blueprint('main', __name__)


@bp.route('/')
def hello_world():
    return 'Hello World!'


@bp.get('/teams')
def get_teams():
    teams = Team.collection.fetch()
    return json.dumps([team.to_dict() for team in teams if team is not None])


@bp.post('/teams')
def create_or_update_teams():

    teams_from_csv: List[Team] = csv_loader.read_teams_info_from_csv()

    team_names = []

    for team in teams_from_csv:
        team.save(merge=True)
        team_names.append(team.team_name)

    return f"Teams created or updated:\n{team_names}", 201
