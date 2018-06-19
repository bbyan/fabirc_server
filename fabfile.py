#!/bin/python
# coding:uft-8
from fabric import SerialGroup as Group
import ConfigParser
import os

from blessings import Terminal

t = Terminal()


def run_command(command_section, connection):
    for option in cf.options(command_section):
        result = connection.run(cf.get(command_section, option), warn=True)
        if option.find('grep', 0) != -1 and result.stdout == '':
            print(option + " exec complete!")


if __name__ == '__main__':
    cf = ConfigParser.ConfigParser()
    # Test env
    # cf.read('command.conf')
    # Prod env
    cf.read(os.path.dirname(os.path.realpath(__file__)) + "command.conf")
    for aims_connection in Group('test@10.99.1.24'):
        print t.red_underline_bold(str(aims_connection))
        run_command("common_command", aims_connection)
        run_command("aims_command", aims_connection)

    for ib_connection in Group('test2@10.99.1.27'):
        print t.red_underline_bold(str(ib_connection))
        run_command("common_command", ib_connection)
        run_command("ib_command", ib_connection)
