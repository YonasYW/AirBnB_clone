#!/usr/bin/python3
"""Define the class named City."""
from models.base_model import BaseModel


class City(BaseModel):
    """It define data of location of user as city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.

    """

    state_id = ""
    name = ""
