#!/usr/bin/python3
"""First User class module"""
from models.base_model import BaseModel
import models

class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """class constructor that initializes the class"""
        super().__init__(*args, **kwargs)
