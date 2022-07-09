#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """BaseModel frame class"""
    def __init__(self, *args, **kwargs):
        """constructor of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """returns name of class, id of instance and dictionay with attr"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to dict """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
