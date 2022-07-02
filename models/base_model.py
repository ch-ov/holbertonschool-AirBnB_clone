#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
def __str__(self):
    print (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

