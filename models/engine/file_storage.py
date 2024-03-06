#!/usr/bin/python3
"""Contain class named Filestorage."""
import json
import os
from models.base_model import BaseModel

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
        key = "{}.{}".format(class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file(path:__file_path)."""
        with open(FileStorage.__file_path, 'w') as f:
            dic_t = {key: val.to_dict() for key, val in FileStorage.__objects.items()}
            json.dump(dic_t, f)

    def reload(self):
        """Deserialize the JSON file to__objects if the file exist."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                dic_t = json.load(f)
                obj_dic = {}
                for val in dic_t.values():
                    cl_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(cl_name)(**val))

