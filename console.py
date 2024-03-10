#!/usr/bin/python3
"""Class Consl is cmd interpreter for airbnb."""
import cmd
import shlex
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The class were console or cmd interpreter define at."""

    prompt = "(hbnb) "
    cl = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def default(self, arg):
        """Last behaviour for the console when there is no cmd at 1st arg."""
        com_list = {
            "all": self.do_all,
            "show": self.do_show,
            "count": self.do_count,
            "destroy": self.do_destroy,
            "update": self.do_update
                }
        if '.' in arg:
            argv = arg.split('.')
            name_cm = str(argv[1].strip('()'))
            cl_n = argv[0]
            match = re.search(r'\((.*?)\)', argv[1])

            if "show" in name_cm:
                class_id = match.group(1)
                return com_list[show](cl_n)(class_id)
            elif ((name_cm not in com_list.keys())
                    or (cl_n not in HBNBCommand.cl)):
                print("** Unkown syntax: {} ***".format(arg))
                return
            else:
                return com_list[name_cm](cl_n)

    def emptyline(self):
        """Do nothing when there is no command or empty line."""
        pass

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_create(self, line):
        """Create a new inst BaseModel,saves it to JSON and prints the id."""
        if line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.cl:
            print("** class doesn't exist **")
        else:
            class_name = line.strip()
            n_model = globals()[class_name]()
            n_model.save()
            print("{}".format(n_model.id))

    def do_show(self, line):
        """Print the string rep __str of inst based on class name,id."""
        argv = line.split()
        len_arg = len(argv)
        all_arg = storage.all()

        if line == "":
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.cl:
            print("** class doesn't exist **")
        elif len_arg == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argv[0], argv[1]) not in all_arg:
            print("** no instance found **")
        else:
            print(all_arg["{}.{}".format(argv[0], argv[1])].__str__())

    def do_destroy(self, line):
        """Delete an instance based on the class name and id."""
        argv = line.split()
        len_arg = len(argv)
        all_arg = storage.all()

        if line == "":
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.cl:
            print("** class doesn't exist **")
        elif len_arg == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argv[0], argv[1]) not in all_arg:
            print("** no instance found **")
        else:
            del all_arg["{}.{}".format(argv[0], argv[1])]
            BaseModel.save(self)

    def do_all(self, line):
        """Print all __str__ of all instances based or not class name."""
        list_str = []
        dict_v = storage.all()

        if len(line) != 0:
            if line not in HBNBCommand.cl:
                print("** class doesn't exist **")
            else:
                for key, val in dict_v.items():
                    k = key.split('.')[0]
                    if k == line:
                        list_str.append(val.__str__())
                print("{}".format(list_str))
        else:
            for key, val in dict_v.items():
                k = key.split('.')[0]
                if k in HBNBCommand.cl:
                    list_str.append(val.__str__())
            print("{}".format(list_str))

    def do_update(self, line):
        """Update an instance based on class name and id."""
        argv = shlex.split(line)
        dict_all = storage.all()

        if len(line) == 0:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.cl:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argv[0], argv[1]) not in dict_all.keys():
            print("** no instance found **")
        elif len(argv) == 2:
            print("** attribute name missing **")
        elif (len(argv) == 3):
            try:
                type(eval(argv[2])) != dict
            except NameError:
                print("** value missing **")
        else:
            key = "{}.{}".format(argv[0], argv[1])
            inst = dict_all[key]
            if argv[1] in ["id", "created_at", "updated_at"]:
                return
            setattr(inst, argv[2], argv[3])
            inst.save()

    def do_count(self, line):
        """Count the number of instances of a class print the number."""
        count = 0
        dict_all = storage.all()

        for key in dict_all.keys():
            if key.split(".")[0] in line:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
