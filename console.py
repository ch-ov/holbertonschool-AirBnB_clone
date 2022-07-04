#!/usr/bin/python3
"""Main connsole for the system app"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class initialized as Command Prompt with module 'cmd'"""

    prompt = "(hbnb) >>> "

    def do_quit(self, arg):
        """Quit Command to exit the Console"""
        exit(0)

    def do_EOF(self, arg):
        """Quit Command to exit the Console"""
        exit(0)

    def emptyline(self):
        """Executes when an empty line is found in the prompt"""
        pass


if __name__ == '__main__':
    """Stops other modules from starting before this main program"""
    HBNBCommand().cmdloop()
