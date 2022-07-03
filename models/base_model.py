#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = dict(self.__dict__)
        dictionary.update({"__class__": self.__class__.__name__,
                           "created_at": str(((self.created_at).isoformat())),
                           "updated_at": str(((self.updated_at).isoformat()))})
        return dictionary
