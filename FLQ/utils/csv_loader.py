import csv
from typing import List
import os

from models.Team import Team


def read_teams_info_from_csv() -> List[Team]:
    """Reads the teams info from a csv file and returns a list of Team objects

    Returns:
        List[Team.Team]: A list of Team objects
    """
    teams = []
    file_path = os.getenv("TEAMS_CSV_PATH")
    if not file_path:
        raise Exception("TEAMS_CSV_PATH environment variable not set")

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        teams = []

        for row in reader:
            team = Team(  # This is used to serialize the data from the csv file into a Team object and make sure it is valid
                team_name=row['team_name'],
                img_id=row['img_id'],
                logo_img_path=row['logo_img_path'],
                alt_names=row['alt_names'].split(',')
            )

            if team:
                teams.append(team)
    return teams
