#!/usr/bin/python3
""" Main connsole for the system app """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Class initialized as Command Prompt with module 'cmd' """

    prompt = "(hbnb) >>> "


if __name__ == '__main__':
    """ Stops other modules from starting before this main program """
    HBNBCommand().cmdloop()
