#!/usr/bin/python3
"""Contain class named Filestorage."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serialize and deserialize JSON file <-> instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, getattr(obj, "id"))
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file(path:__file_path)."""
        dic_t = {}

        for key, val in FileStorage.__objects.items():
            dic_t[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dic_t, f)

    def reload(self):
        """Deserialize the JSON file to__objects if the file exist."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                dic_t = json.load(f)
                for val in dic_t.values():
                    cl = val["__class__"]
                    obj_dic = globals().get(cl)
                    obj = obj_dic(**val)
                    self.new(obj)
