#!/usr/bin/python3
"""Define a class named Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent the review given by user.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.

    """

    place_id = ""
    user_id = ""
    text = ""
