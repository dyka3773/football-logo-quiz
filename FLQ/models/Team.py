import fireo
import os
from fireo.models import Model
from fireo.fields import TextField, NumberField, ListField, IDField
from typing import List, Optional

from utils.base64_util import img_to_base64

fireo.connection(from_file=os.getenv("FIREBASE_CONFIG_PATH"))


class Team(Model):
    id = IDField()
    team_name = TextField()
    img_id = NumberField()
    logo = TextField()
    alt_names = ListField()


def create_team(team_name: str, img_id: int, logo_img_path: str, alt_names: List[str]) -> Optional[Team]:
    """Create a team and save it to the database

    Args:
        team_name (str): The name of the team
        img_id (int): The id of the team's logo
        logo_img_path (str): The path to the team's logo
        alt_names (List[str]): A list of alternative names for the team

    Returns:
        Team: The created team
    """
    logo = img_to_base64(logo_img_path)
    team = Team.collection.create(
        id=str(img_id),
        team_name=team_name,
        img_id=img_id,
        logo=logo,
        alt_names=alt_names
    )
    return team
