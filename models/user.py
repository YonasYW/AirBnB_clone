#!/usr/bin/python3
"""Contain class name 'user' that inherit from class 'BaseModel'."""
from models.base_model import BaseModel


class User(BaseModel):
    """User is a class with instance of user data."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
