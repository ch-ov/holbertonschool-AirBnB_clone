#!/usr/bin/python3
"""Amenity class module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor that initializes the class"""
        super().__init__(*args, **kwargs)
