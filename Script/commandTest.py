from Bash.command import Command
import random

command = Command()


@command.add(only_one_value=str)
def rand(value):
    value = value.split(":")
    print('random number:', random.randint(int(value[0]), int(value[1])))
