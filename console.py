#!/usr/bin/python3
"""Main connsole for the system app"""

import cmd
import models
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Class initialized as Command Prompt with module 'cmd'"""

    prompt = "(hbnb) >>> "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit Command to exit the Console"""
        exit(0)

    def do_EOF(self, arg):
        """Quit Command to exit the Console"""
        exit(0)

    def emptyline(self):
        """Executes when an empty line is found in the prompt"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""

        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
            return
        
        elif arg[0] in HBNBCommand.classes:
            newobject = eval(arg[0])()

        else:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """Will show the """
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
            return

        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif len(arg) < 2:
            print("** instance id missing **")
            return

        else:
            dict_all_obj = storage.all()
            string = f'{arg[0]}.{arg[1]}'

            if string not in dict_all_obj.keys():
                print("** no instance found **")

            else:
                print(dict_all_obj[string])

    def destroy(self, arg):
        """Will delete an instance based on the class 'name' & 'id'"""
        arg = arg.split()

        if len(arg) <= 1:
            print("** class name missing **")
            return

        if arg(0) not in classes:
            print("** class doesn't exits **")
            return

        elif len(arg) < 2:
            print("** instance is missing **")
            return

        dict = storage.all()
        for key, value in dict.items():
            if f"{arg[0]}.{arg[1]}" == key:
                del dict[key]
                storage.save()
                return

        print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        arg = arg.split()

        if len(arg) == 0:
            obj_dict = storage.all()
            str_list = []
            for key, value in obj_dict.items():
                str_list.append(str(value))
            print(str_list)
            return
        try:
            inst = eval(arg[0])()    
        except:
            print("** class doesn't exist **")
            return

        obj_dict = storage.all()
        str_list = []
        for key, value in obj_dict.items():
            if arg[0] in key:
                str_list.append(str(value))

    def do_update(self, arg):
        """Prints all string representation of all instances"""
        arg = arg.split()

        if len(arg) <= 1:
            print("** class name missing **")
            return
        try:
            inst = eval(arg[0])()    
        except:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id is missing **")
            return

        if len(arg) < 3:
            print("** attribute name is missing **")
            return

        if len(arg) < 4:
            print("** value missing **")
            return

        if len(arg) > 4:
            arg = arg[:3]

        dict = storage.all()
        for key, value in dict.items():
            if f"{arg[0]}.{arg[1]}" == key:
                if type(arg[3]) is int:
                    setattr(value, arg[2], int(arg[3]))
                elif type(arg[3]) is float:
                    setattr(value, arg[2], float(arg[3]))
                else:
                    setattr(value, arg[2], str(arg[3]))
        storage.save()


if __name__ == '__main__':
    """Stops other modules from starting before this main program"""
    HBNBCommand().cmdloop()
