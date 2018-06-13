from fabric import SerialGroup as Group
import ConfigParser
from blessings import Terminal


def run_command(command_section):
    for option in cf.options(command_section):
        connection.run(cf.get(command_section, option), warn=True)


if __name__ == '__main__':
    cf = ConfigParser.ConfigParser()
    cf.read('command.conf')
    t = Terminal()
    for connection in Group('ibuser@10.211.55.101', 'ibuser@10.211.55.101'):
        print t.red_underline_bold(str(connection))
        run_command("common_command")
