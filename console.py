#!/usr/bin/python3
"""Main connsole for the system app"""

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """Class initialized as Command Prompt with module 'cmd'"""
    prompt = "(hbnb) >>> "
    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User}

    def do_quit(self, arg):
        """Quit Command to exit the Console"""
        exit(0)

    def do_EOF(self, arg):
        """Quit Command to exit the Console"""
        print()
        exit(0)

    def emptyline(self):
        """Executes when an empty arg is found in the prompt"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""

        if len(arg) == 0:
            print("** class name missing **")

        elif arg not in self.classes:
            print("** class doesn't exist **")

        else:
            for key, clas in self.classes.items():
                if arg == key:
                    obj = clas()
                    obj.save()
                    print(obj.id)

    def do_show(self, arg):
        """Prints an instance according to given id"""
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")

        else:
            if arg[0] in self.classes:

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
            print("** class doesn't exist **")

        elif len(arg) < 2:
            print("** instance is missing **")

        elif arg[0] in self.classes:
            if len(arg) > 1:
                objects = storage.all()
                flag = None
                for key in objects.keys():
                    if str(arg[1]) in key:
                        flag = key
                if flag:
                    del(objects[flag])
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objects = storage.all()
        list_obj = []

        if len(arg) == 0:
            for key, vals in objects.items():
                list_obj.append(str(vals))
            print(list_obj)

        elif arg in self.classes:
            for keys, vals in objects.items():
                if vals.__class__.__name__ == arg:
                    list_obj.append(str(vals))
            print(list_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update command to add or update attributes"""
        args = arg.split()

        if len(args) == 0:
            print('** class name missing **')

        elif args[0] not in self.classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print('** instance id missing **')

        elif len(args) == 3:
            print("** value missing **")

        else:
            obj_name = '{}.{}'.format(args[0], args[1])
            obj_dict = storage.all()
            if obj_name in obj_dict.keys():
                if len(args) == 2:
                    print("** attribute name missing **")

                else:
                    value = args[3].replace('"', '')
                    object = obj_dict.get(obj_name)
                    object.__setattr__(args[2], value)
                    storage.save()
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Counts the number of objects stored in the .json"""
        lists = arg.split()
        count = 0
        for classes in models.storage.all().values():
            if lists[0] == classes.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    """Stops other modules from starting before this main program"""
    HBNBCommand().cmdloop()
