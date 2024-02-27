import fireo
import os
import logging
from fireo.models import Model
from fireo.fields import TextField, NumberField, ListField, IDField
from typing import List, Optional

from utils.base64_util import img_to_base64

fireo.connection(from_file=os.getenv("FIREBASE_CONFIG_PATH"))

logger = logging.getLogger(__name__)


class Team(Model):
    id = IDField()
    team_name = TextField()
    img_id = NumberField()
    logo = TextField()
    alt_names = ListField()
    difficulty = NumberField()


def create_team(team_name: str, img_id: int, logo_img_path: str, alt_names: List[str], difficulty: str) -> Optional[Team]:
    """Create a team and save it to the database

    Args:
        team_name (str): The name of the team
        img_id (int): The id of the team's logo
        logo_img_path (str): The path to the team's logo
        alt_names (List[str]): A list of alternative names for the team
        difficulty (str): How difficult to know the team is (0-100 where 0 is the easiest and 100 is the hardest)

    Returns:
        Team: The created team
    """
    try:
        logo = img_to_base64(logo_img_path)
    except FileNotFoundError as e:
        logger.error("Error while trying to find the logo for team" +
                     f" {team_name} with img_id {img_id}: \n{e}")
        raise e

    team = Team.collection.create(
        id=str(img_id),
        team_name=team_name,
        img_id=img_id,
        logo=logo,
        alt_names=alt_names,
        difficulty=int(difficulty)
    )

    return team
