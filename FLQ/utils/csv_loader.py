import csv
from typing import List
import os

from models import Team


def read_teams_info_from_csv() -> List[Team.Team]:
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
            logo_img_path = row['logo_img_path']
            img_id = get_img_id(logo_img_path)
            alt_names = row['alt_names'].split(',')
            if alt_names == ['']:
                alt_names = []

            team = Team.create_team(  # This is used to serialize the data from the csv file into a Team object and make sure it is valid
                team_name=row['team_name'],
                img_id=img_id,
                logo_img_path=logo_img_path,
                alt_names=alt_names
            )

            if team:
                teams.append(team)
    return teams


def get_img_id(img_path: str) -> int:
    """Gets the img_id from the img_path
    WARNING: This function assumes that the img_id is the last part of the img_path and that the img_path is a string with the format: 'path/to/img/img_id.jpg'

    Args:
        img_path (str): The path to the image

    Returns:
        int: The img_id
    """
    if os.name == 'nt':
        return int(img_path.split('\\')[-1].split('.')[0])
    else:
        return int(img_path.split('/')[-1].split('.')[0])
