#!/usr/bin/python3
"""
Module containing the entery point of the Command interpreter
"""
import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Reviews
from models.state import State
from models.user import User


classes = {"Amenity":Amenity, "BaseModel":BaseModel, "City":City,
                   "Place":Place, "Reviews":Reviews, "State":State,
                   "User":User}

class HBNBCommand(cmd.Cmd):
    """
    HBNHCommand - Console class

    Args:
        cmd (SuperClass): cmd class
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        do_quit - quit console

        Args:
            line (str): console input

        Returns:
            Bool: True to exit console
        """
        return True

    def do_EOF(self, line):
        """
        do_EOF - handles end of file

        Args:
            line (str): console input

        Returns:
            Bool: True to exit console
        """
        return True

    def do_create(self, line):
        """
        do_create - creates new object

        Args:
            line (string): user input indicating which ibject to create
        """
        if len(line.strip()) > 0:
            tmp = line.strip().split(" ")
            cmd = ""
            if len(tmp) > 1:
                cmd = tmp[0]
            else:
                cmd = line
            if cmd in classes.keys():
                for key, value in classes.items():
                    if key == cmd:
                        tmp_obj = value()
                print(tmp_obj.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        do_show - Shows an object str representation based on id and object name

        Args:
            line (str): user input containing object class and object id
        """
        if len(line.strip()) > 0:
            tmp = line.strip().split(" ")
            if len(tmp) == 1:
                print("** instance id missing **")
            else:
                try:
                    cls = tmp[0]
                    id = tmp[1]
                    if cls in classes.keys():
                        tmp = cls + "." + id
                        tmp_dict = models.storage.all()
                        print(tmp_dict[tmp])
                    else:
                        print("** class doesn't exist **")
                except KeyError:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        do_destroy - destrys/ deletes an object based on it class name and Id

        Args:
            line (string): user input containing object class and object id
        """
        if len(line.strip()) > 0:
            tmp = line.strip().split(" ")
            if len(tmp) == 1:
                print("** instance id missing **")
            else:
                try:
                    cls = tmp[0]
                    id = tmp[1]
                    if cls in classes.keys():
                        tmp = cls + "." + id
                        tmp_dict = models.storage.all()
                        del tmp_dict[tmp]
                        models.storage.save()
                    else:
                        print("** class doesn't exist **")
                except KeyError:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        do_all - print all objects created

        Args:
            line (string): user input containing object class and object id
        """
        if len(line.strip()) > 0:
            tmp = line.strip().split(" ")
            cls = ""
            tmp_list = list()
            if len(tmp) > 1:
                cls = tmp[0]
            else:
                cls = line
            if cls in classes.keys():
                for key, value in models.storage.all().items():
                    if cls in key:
                        tmp_list.append(str(value.to_dict()))
                print(tmp_list)
            else:
                print("** class doesn't exist **")
        else:
            tmp_list = list()
            for key, value in models.storage.all().items():
                    tmp_list.append(str(value.to_dict()))
            print(tmp_list)

    def do_update(self, line):
        """
        do_update - updates an object new/existing attribute

        Args:
            line (string): user input containing object class, id, attribute and value
        """
        if len(line.strip()) > 0:
            tmp = line.strip().split(" ")
            count = len(tmp)
            if count == 1:
                print("** instance id missing **")
            elif count == 2:
                print("** attribute name missing **")
            elif count == 3:
                print("** value missing **")
            else:
                try:
                    cls = tmp[0]
                    key = str(tmp[0]) + "." + str(tmp[1])
                    att = tmp[2]
                    new_val = tmp[3]
                    if cls in classes.keys():
                        setattr(models.storage.all()[key], att, new_val)
                        models.storage.save()
                    else:
                        print("** class doesn't exist **")
                except KeyError:
                    print("** no instance found **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
