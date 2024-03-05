#!/usr/bin/python3
"""Class console is cmd interpreter for airbnb."""
import cmd


class Console(cmd.Cmd):
    """The class were console or cmd define at."""

    prompt = "(hbnb) \n"

    def do_EOF(self, line):
        """It will exit when cntrl+d command run."""
        return True

    def do_quit(self, line):
        """It will exit when cntrl+d command run."""
        return True

    """def help_EOF(self, line):
        "Documentation for command EOF."
        print()"""
if __name__ == "__main__":
    Console().cmdloop()
