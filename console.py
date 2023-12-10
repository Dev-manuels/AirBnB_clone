#!/usr/bin/python3
"""
Module containing the entery point of the Command interpreter
"""
import cmd
from models.base_model import BaseModel


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
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
