#!/usr/bin/python
"""5. Store first object"""
import json
import models
from datetime import datetime


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
        for x in self.__objects:
            dict[x] = self.__objects[x].to_json()

        with open(self.__file_path, "w") as file:
            json.dump(dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        pass
