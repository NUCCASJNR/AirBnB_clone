#!/usr/bin/python3
"""This module contains the console.py module"""
from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """The class HBNB that builds a console"""

    prompt = "(hbnb)"
    CLASSNAMES = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_create(self, arg):
        tokens = arg.split(" ")
        if arg == "":
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.CLASSNAMES:
            print("** class doesn't exit **")
        else:
            print(eval(tokens[0])().id)
            storage.save()

        # print(len(tokens))

    def do_EOF(self, arg):
        """Handles EOF"""

        raise systemExit

    def emptyline(self):
        """This doesnt do anything when the no command is passed"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
