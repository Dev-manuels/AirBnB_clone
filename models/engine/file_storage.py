#!/usr/bin/python3
"""
Module containing class FileStorage
"""


class FileStorage():
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return (self.__objects)

    def new(self, obj):
        key = str(obj.__class__.___name__) + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        print("save")

    def reload(self):
        print("reload")
