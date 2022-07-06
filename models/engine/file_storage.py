#!/usr/bin/python
"""5. Store first object"""
import models
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """serializes and deserializes instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            self.__objects[obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                for key, value in ((json.load(file)).items()):
                    value = eval(value["__class__"])(**value)
                self.__objects[key] = value
        except Exception:
            pass
