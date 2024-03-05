#!/usr/bin/python3
"""Contain class named BaseModel."""
import uuid
from datetime import datetime

class BaseModel():
    """Define all common attributes or methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize the instance into object."""
        if len(kwargs) != 0:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__[key] = datetime.strptime(
                            kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                            kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Print string represention of object."""
        return "[{}] ({}) {}".\
                format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the time instance updated_at each time a change."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing __dict__ of the instance"""
        ins_dict = self.__dict__.copy()
        ins_dict['__class__'] = self.__class__.__name__
        ins_dict["created_at"] = ins_dict["created_at"].isoformat()
        ins_dict["updated_at"] = ins_dict["updated_at"].isoformat()
        return ins_dict
