#!/usr/bin/python3
"""
Module containing class Reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Reviews - class Reviews

    Args:
        BaseModel (SuperClass): parent class of class Reviews
    """
    place_id = ""
    user_id = ""
    text = ""
