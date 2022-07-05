#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel frame"""
    def __init__(self, *args, **kwargs):
        """constructor of BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key in "__class__":
                    continue

    def __str__(self):
        """returns name of class, id of instance and dictionay with attr"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public attribute updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary with keys/values of __dict__ of the instance"""
        dictionary = dict(self.__dict__)
        dictionary.update({"__class__": self.__class__.__name__,
                           "created_at": str(((self.created_at).isoformat())),
                           "updated_at": str(((self.updated_at).isoformat()))})
        return dictionary
