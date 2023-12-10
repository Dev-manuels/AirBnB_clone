#!/usr/bin/python3
"""
Module containing the BaseModel class
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """BaseModel
    BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """__init__
        class BaseModel constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    self.__setattr__(key, value)
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        __str__
        String representation of an object

        Returns:
            string: object representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save
        updates the updated_at instance variable
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        to_dict - created a dictionary of all object attributes

        Returns:
            dict: dict to be used for serialization
        """
        tmp_dict = dict(self.__dict__)
        tmp_dict.update({"__class__": self.__class__.__name__})
        tmp_dict.update({"created_at": self.created_at.isoformat()})
        tmp_dict.update({"updated_at": self.updated_at.isoformat()})
        return tmp_dict
