#!/usr/bin/python3
"""This module contains the console.py module"""

from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """The class HBNB that builds a console"""

    prompt = "(hbnb) "
    CLASSNAMES = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """

        tokens = arg.split(" ")
        if arg == "":
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.CLASSNAMES:
            print("** class doesn't exit **")
        else:
            print(eval(tokens[0])().id)
            storage.save()

        # print(len(tokens))

    def do_show(self, arg):
        """ Prints the string representation of an instance
        based on the class name and id
        """

        tokens = arg.split()
        if arg == "":
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.CLASSNAMES:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(tokens[0], tokens[1])
            if key not in storage.all():
                print("**no instance found**")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """: Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """

        tokens = arg.split()
        if arg == "":
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.CLASSNAMES:
            print("* class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(tokens[0], tokens[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or
        not on the class name. Ex: $ all BaseModel or $ all.
        The printed result must be a list of strings (like the example below)
        If the class name doesn’t exist, print ** class doesn't exist **
        (ex: $ all MyModel)
        """

        tokens = arg.split()
        if len(tokens) == 0:
            print([str(value) for value in storage.all().values()])
        elif tokens[0] not in HBNBCommand.CLASSNAMES:
            print("** class doesn't exist **")
        else:
            temp = [str(v) for k, v in storage.all().items()
                    if k.startswith(tokens[0])]
            print(temp)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file). Ex: $ update BaseModel 1234-1234-1234
        email "aibnb@mail.com".
        """

        tokens = arg.split()
        if arg == "":
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.CLASSNAMES:
            print("* class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")


    def do_EOF(self, arg):
        """Handles EOF"""

        raise systemExit

    def emptyline(self):
        """This doesnt do anything when the no command is passed"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
