#!/usr/bin/python3
"""
Module containing class FileStorage
"""
import json
import os


class FileStorage():
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return (self.__objects)

    def new(self, obj):
        key = str(obj.__class__.__name__) + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        new_dict = dict()
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(new_dict))

    def reload(self):
        from models.base_model import BaseModel
        tmp_dict = dict()
        try:
            if os.stat(self.__file_path).st_size > 0:
                with open(self.__file_path, encoding="utf-8") as file:
                    tmp_dict = json.load(file)
                for key, value in tmp_dict.items():
                    self.__objects[key] = BaseModel(value)
        except FileNotFoundError:
            pass
