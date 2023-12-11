#!/usr/bin/python3
"""
Module contaning class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City - City class

    Args:
        BaseModel (SuperClass): parent class of class City
    """
    state_id = ""
    name = ""
