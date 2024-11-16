#!/usr/bin/python3
"""Store first object"""
from models.base_model import BaseModel
import os
import json


class FileStorage:
    """serialize instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary"""
        return (FileStorage.__objects)

    def new(self, obj):
        """Set obj with key <obj class name>.id"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __object to JSON file"""
        obj_dict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as json_file:
                obj_dict = json.load(json_file)
                for obj in obj_dict.values():
                    class_descr = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_descr)(**obj))
