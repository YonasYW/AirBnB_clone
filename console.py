#!/usr/bin/python3
"""Class HBNBCommand is cmd interpreter for airbnb."""
import cmd


class HBNBCommand(cmd.Cmd):
    """The class were console or cmd interpreter define at."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
