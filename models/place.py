#!/usr/bin/python3
"""
Module containing class Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place - Place class

    Args:
        BaseModel (SuperClass): parent class of class Place
    """
    city_id = ""
    user_id = ""
    name = ""
    desxription = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longtitude = 0.0
    amenity_ids = list()
