#!/usr/bin/python3
"""command line interpreter that stores objet data in json files"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """the clone console interpreter class"""

    prompt = "(hbnb) "
    __classes_HBNB = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """ Creates a new instance of Class,
        saves it (to the JSON file) and prints the id
        """
        args: list = line.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_HBNB:
            print("** class doesn't exist **")
        else:
            instance_Data_file = FileStorage()
            instance = HBNBCommand.__classes_HBNB[args[0]]()
            print(instance.id)
            instance_Data_file.new(instance)
            instance_Data_file.save()

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id
        """
        args: list = line.split()
        instance_Data_file = FileStorage()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_HBNB:
            print("** class doesn't exist **")
        else:
            if not args[1]:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                instance_Data = instance_Data_file.all()
                if key in instance_Data:
                    print(instance_Data[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name
         and id (save the change into the JSON file)
         """
        args: list = line.split()
        instance_Data_file = FileStorage()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_HBNB:
            print("** class doesn't exist **")
        else:
            if not args[1]:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                instance_Data = instance_Data_file.all()
                if key in instance_Data:
                    del instance_Data[key]
                    instance_Data_file.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of
        all instances based or not on the class name
        """
        args: list = line.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_HBNB:
            print("** class doesn't exist **")
        else:
            instance_Data_file = FileStorage().all()
            instance_list = []
            for i in instance_Data_file.values():
                instance_list.append(i.__str__())
            print(instance_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute
        (save the change into the JSON file)
        """
        args = line.split()
        instance_Data_file = FileStorage()

        if not line:
            print("** class name missing **")
        else:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
            elif f"{class_name}.{args[1]}" not in instance_Data_file.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                instance_Data = instance_Data_file.all().get(f"{class_name}.{args[1]}")

                if instance_Data:
                    setattr(instance_Data, args[2], args[3])
                    instance_Data.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
