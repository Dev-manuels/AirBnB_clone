#!/usr/bin/python3
"""
Module contaning class User
"""
from base_model import BaseModel


class User(BaseModel):
    """
    User - user class subclass of BaseModel

    Args:
        BaseModel (SuperClass): base class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
