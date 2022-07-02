#!/usr/bin/python3
""" Main connsole for the system app """

import os

cmd_list = ["help", "quit", "EOF"]

def welcome_menu():
    """ Displays a Welcome menu for start """
    print("""+------------------------------------+
|    Welcome to the HBNB Console!    |
+------------------------------------+
    """)

def help_menu():
    """ Displays a dictionary of Commands """
    print("""
Documented commands (type help <topic>):
========================================""")
    print(dict)

welcome_menu()

dict = ["help", "info", "contact"]

while True:
    cmd = input("(hbnb) >>> ")
    if cmd == 'help':
        help_menu()
    if cmd == 'quit':
        exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
