#!/usr/bin/python3
"""Main connsole for the system app"""

import cmd
import models
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Class initialized as Command Prompt with module 'cmd'"""

    prompt = "(hbnb) >>> "
    classes = {"BaseModel": BaseModel,}

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

        if len(arg) == 0:
            print("** class name missing **")

        elif arg not in self.classes:
            print("** class doesn't exist **")

        else:
            new_inst = eval(arg)()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        """Prints an instance according to given id"""
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")

        else:
            if arg[0] in self.classes.keys():

                if len(arg) == 1:
                    print("** instance id missing **")

                else:
                    objects = storage.all()
                    flag = None

                    for key in objects.keys():
                        if str(arg[1]) in key:
                            flag = key

                    if flag:
                        print(objects[flag])

                    else:
                        print("** no instance found **")

            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Will delete an instance based on the class 'name' & 'id'"""
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")

        elif arg[0] not in self.classes:
            print("** class doesn't exits **")

        elif len(arg) < 2:
            print("** instance is missing **")

        elif arg[0] in self.classes:
            if len(arg) > 1:
                key = arg[0] + "." + arg[1]
                if key in models.storage.all():
                    del (models.storage.all[key])
                    models.storage.save()

        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        dict_all_obj = storage.all()
        list_obj = []

        if len(arg) == 0:
            for key, vals in dict_all_obj.items():
                list_obj.append(str(vals))
            print(list_obj)

        elif arg in self.classes:
            for keys, vals in dict_all_obj.items():
                if vals.__class__.__name__ == arg:
                    list_obj.append(str(vals))
            print(list_obj)
        else:
            print("** class doesn't exist **")

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
