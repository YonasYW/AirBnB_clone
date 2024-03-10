#!/usr/bin/python3
"""Defines a class named State."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent the location of user as state name.

    Attributes:
        name (str): The name of the state.

    """

    name = ""
