from Bash.command import Command


command = Command()

"""
When I put just one key

packageX64 -version

the program put an error:
    File "/home/winstonwolf007/Prog/python/YouTube-Shield/Bash/bash.py", line 15, in run
        param[el] = x[1:][y+1]
        IndexError: list index out of range
"""


@command.add(only_one_value=str)
def mkdir(val):
    print(val)


@command.add(bits=int, app=str)
def file(val):
    print(val)


@command.add(only_one_param='v')
def node():
    print('V17.9.0')
