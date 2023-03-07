#!/usr/bin/python3
"""This module contains the console.py module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The class HBNB that builds a console"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """Handles EOF"""

        raise systemExit

    def emptyline(self):
        """This doesnt do anything when the no command is passed"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
